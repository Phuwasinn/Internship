import json, logging

logging.basicConfig(level = logging.DEBUG)

def load_config(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
     
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return None
    
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in file: {filepath}")
        return None       

    required_keys = ["host", "port", "database"]
    for key in required_keys:
        if key not in data:
            logging.warning(f"Missing key: {key} in config")            

    logging.info("Config loaded succesfully")
    return data

import os
with open("config.json", "w") as f:
    json.dump({"host": "localhost", "port": 5432, "database": "mydb"}, f)

config = load_config("config.json")
print("Config:", config)

load_config("nonexistent.json")

os.remove("config.json")