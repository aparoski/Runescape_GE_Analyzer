import kaggle
import config
import subprocess
import os, json, subprocess



#need the most recently updated folder which should contain the newly updated dataset. 

def most_recent_local_dataset():
    """returns the latest updated runescape dataset folder path
    as a string"""
    data_files = os.listdir(config.upper_dir)
    paths = [os.path.join(config.upper_dir, folder) for folder in data_files]
    recent_folder = max(paths, key = os.path.getctime)

    return(recent_folder)


#def runescape_dataset_upload(data):

# there should only be one dataset for runescape written by myself...for now
datasets = kaggle.api.dataset_list(search = "aparoski/Runescape")

Rune_Dat = datasets[0]

Rune_Dat

Rune_Dat_Files = kaggle.api.dataset_create_version_cli()



if __name__ == "__main__":
    print()