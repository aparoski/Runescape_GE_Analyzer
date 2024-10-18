import subprocess
import config
import gen_funcs



#need the most recently updated folder which should contain the newly updated dataset. 




#def runescape_dataset_upload(data):

# there should only be one dataset for runescape written by myself...for now

dataset_name = "aparoski/runescape-grand-exchange-data"

dataset_path = gen_funcs.most_recent_local_dataset()

# p1 = subprocess.run("kaggle datasets init -p " + dataset_path, 
#                     shell = True)

# print(p1.returncode)



if __name__ == "__main__":
    print(most_recent_local_dataset())