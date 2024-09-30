import kaggle
import subprocess


test = subprocess.run(["cmd.exe", "kaggle datasets list -s 'fraud detection'"],
               capture_output = True, text = True, shell = True)


print(test)