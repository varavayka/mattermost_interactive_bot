from pathlib import Path
import json
def config_reader(folder_config, file):
    path = Path(folder_config, file)
    with open(path, 'r') as config:
        return json.loads(config.read())

# print(config_reader('config', 'description.json'))