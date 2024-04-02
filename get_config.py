import json
import sys
def get_config(path_to_config='./config.json'):
    try:
        with open(path_to_config, 'r', encoding='utf-8') as config:
         return json.loads(config.read())
        
    except IOError as e:
        print(f'Unable to read config! Reason: {e}')
        sys.exit(1)