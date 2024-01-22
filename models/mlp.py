import torch.nn as nn
import torch
import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, in_plane, inter_plane, out_class):
        super(MLP, self).__init__()
        self.mlp = nn.Sequential(
                        # nn.Flatten(),
                        nn.Linear(in_plane, inter_plane),
                        nn.ReLU(),
                        nn.Linear(inter_plane, inter_plane),
                        nn.ReLU(),
                        nn.Linear(inter_plane, inter_plane),
                        nn.ReLU()
        )
        self.classifier = nn.Linear(inter_plane, out_class)
        
    def forward(self, x):
        out = self.mlp(x)
        out = out.view(out.size(0), -1)
        logits = self.classifier(out)
        out = F.softmax(logits, dim=1)
        return out, logits