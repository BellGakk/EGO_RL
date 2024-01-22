import csv
import os
import torch
import numpy as np
from smt.applications import EGO
from smt.surrogate_models import KRG
from smt.utils.design_space import DesignSpace
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.stats import qmc
import time
from utils import *
from models.mlp import *
from torch.utils.tensorboard import SummaryWriter

results_pth = './results'
if not os.path.exists(results_pth):
    os.makedirs(results_pth)

path = None
test_case_run = None

if not has_folders(results_pth):
    test_case_run = 'ego_testcase_0'
    path = os.path.join(results_pth, test_case_run+'/')
    os.makedirs(path)
else:
    dir_names = get_folder_names(results_pth)
    idx_run = 0
    for dir_name in dir_names:
        idx_run = max(idx_run, int(dir_name.split('_')[-1]))
    idx_run += 1
    test_case_run = 'ego_testcase_'+str(idx_run)
    path = os.path.join(results_pth, test_case_run+'/')
    if not os.path.exits(path):
        os.mkdirs(path)
init_log_pth = os.path.join(path, 'init.log')

in_plane = 100
inter_plane = 300
out_class = 10
target_softmax = np.random.dirichlet(np.ones(out_class), size=1)    
# LHS settings
number_samples = 5 * in_plane
sampler = qmc.LatinHypercube(d=in_plane)
samples = sampler.random(n=number_samples)
samples = qmc.scale(samples, l_bounds=[0]*in_plane, u_bounds=[1]*in_plane)
criterion_categories = ['EI', 'LCB', 'SBO']
loss = nn.MSELoss()
input_range = [0, 1] 
xlimits = np.array([[input_range[0], input_range[1]] for i in range(in_plane)]) 
model = MLP(in_plane=in_plane, inter_plane=inter_plane, out_class=out_class)
model = model.cuda()

init_logger = Logger(init_log_pth)
init_logger.log('EGO_start')
init_logger.log('We randomly sample {} samples with {} dimensions'.format(number_samples, in_plane))
init_logger.log('The initial samples are listed as below: '+str(samples))
init_logger.log('The target softmax values are listed as below: '+str(target_softmax))

def function_test_100d(X):
    X = torch.from_numpy(X).float()
    Y_list = []
    broadcasted_target_softmax = torch.from_numpy(np.tile(target_softmax, (500, 1))).float()
    X = X.cuda()
    broadcasted_target_softmax = broadcasted_target_softmax.cuda()

    out, logits = model(X)
    
    for i in range(len(out)):
        output_loss = loss(out[i], broadcasted_target_softmax[i])
        Y_list.append(output_loss.cpu().detach().numpy())
    Y_array = np.array(Y_list).reshape(len(Y_list), -1)
    return Y_array

def EGO_start(logger, samples, n_iter, criterion, writer):
    
    design_space = DesignSpace(xlimits)
        
    ego = EGO(
        n_iter=n_iter,
        criterion=criterion,
        xdoe=samples,
        surrogate=KRG(design_space=design_space, print_global=False)
    )
    time_start = time.time()
    x_opt, y_opt, _, x_data, y_data = ego.optimize(fun=function_test_100d)
    time_end = time.time()
    
    logger.log('The iteration number is '+str(n_iter))
    logger.log('The criterion is '+criterion)
    logger.log('The process time is '+str(time_end - time_start))
    logger.log('Optimized input X is '+str(x_opt))
    logger.log('Optimized output y is '+str(y_opt))
    logger.log('The optimized values are '+str(y_data))
    
    idx_iter = 0
    for y_single_data in y_data[-n_iter:][0]:
        idx_iter += 1
        writer.add_scalar(test_case_run+'-'+str(n_iter)+'-'+criterion, float(y_single_data), idx_iter)

if __name__ == '__main__':

    for n_iter in range(100, 201, 50):
        for criterion in criterion_categories:
            writer = SummaryWriter(path)
            EGO_start(init_logger, samples, n_iter, criterion, writer)
            writer.close()