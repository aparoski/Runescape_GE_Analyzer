import os
import config
import datetime

def make_new_recent_folder():
    """creates new folder"""
    dir = config.upper_dir
    today = datetime.datetime.strftime(datetime.date.today(), '%Y-%m-%d')
    os.mkdir(dir + '\\' + "Runescape_GE_Analytics_" + today)





def most_recent_local_dataset():
    """returns the latest updated runescape dataset folder path
    as a string"""
    data_files = os.listdir(config.upper_dir)
    paths = [os.path.join(config.upper_dir, folder) for folder in data_files]
    recent_folder = max(paths, key = os.path.getctime)

    return(recent_folder)

if __name__ == "__main__":
    make_new_recent_folder()