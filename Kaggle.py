import kaggle
import config
import subprocess
import os, json, subprocess

api = kaggle.api
# there should only be one dataset for runescape written by myself...for now
datasets = kaggle.api.dataset_list(search = "aparoski/Runescape")

Runescape_Dataset = datasets[0]


#need the most recently updated folder which should contain the newly updated dataset. 
data_files = os.listdir(config.upper_dir)
paths = [os.path.join(config.upper_dir, folder) for folder in data_files]
oldest_folder = max(paths, key = os.path.getctime)

print(oldest_folder)