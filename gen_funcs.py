import os


def most_recent_local_dataset():
    """returns the latest updated runescape dataset folder path
    as a string"""
    data_files = os.listdir(config.upper_dir)
    paths = [os.path.join(config.upper_dir, folder) for folder in data_files]
    recent_folder = max(paths, key = os.path.getctime)

    return(recent_folder)