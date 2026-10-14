import subprocess
import config
import gen_funcs
import datetime



#need the most recently updated folder which should contain the newly updated dataset. 




#def runescape_dataset_upload(data):

# there should only be one dataset for runescape written by myself...for now

dataset_name = "aparoski/runescape-grand-exchange-data"

dataset_path = gen_funcs.most_recent_local_dataset()

print(dataset_path)

version_note = '"data_scrapped_on_' + datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d') + '"'

command = "kaggle datasets version" + " -p " + dataset_path + " -m " + version_note 

p1 = subprocess.run(command, 
                    shell = True)

print(p1.returncode)



if __name__ == "__main__":
    pass