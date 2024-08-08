import kaggle
import json
import os
import subprocess
import config


def init_on_kaggle(username, api_key):
    KAGGLE_CONFIG_DIR = os.path.join(os.path.expandvars('$HOME'), '.kaggle')
    os.makedirs(KAGGLE_CONFIG_DIR, exist_ok = True)
    api_dict = {"username":username, "key":api_key}
    with open(f"{KAGGLE_CONFIG_DIR}/kaggle.json", "w", encoding='utf-8') as f:
        json.dump(api_dict, f)
    cmd = f"chmod 600 {KAGGLE_CONFIG_DIR}/kaggle.json"
    output = subprocess.check_output(cmd.split(" "))
    output = output.decode(encoding='UTF-8')
    print(output)

init_on_kaggle(config.Kaggle_username, config.Kaggle_API_Key)

api = kaggle.api

print(api.get_config_value(config.Kaggle_username))