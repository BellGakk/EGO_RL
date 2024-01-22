import os
import logging

class Logger(object):
    def __init__(self, path):
        self.logger = logging.getLogger()
        self.path = path
        self.setup_file_logger()
        print ('Logging to file: ', self.path)
        
    def setup_file_logger(self):
        hdlr = logging.FileHandler(self.path, 'w+')
        self.logger.addHandler(hdlr) 
        self.logger.setLevel(logging.INFO)

    def log(self, message):
        print (message)
        self.logger.info(message)

def has_folders(path):
    if not os.path.exists(path):
        return False
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            return True
    return False

def get_folder_names(path):
    folder_names = []
    if os.path.exists(path):
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                folder_names.append(entry)
    return folder_names