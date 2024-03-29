import json
import sys

def get_config_file(path_to_file):
    try:
        with open(path_to_file, 'r', encoding='utf-8') as config:
            return json.loads(config.read())
    except IOError as e:
        print(f'Unable to read config! Reason: {e}')
        sys.exit(1)