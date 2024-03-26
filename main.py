import json
import sys
from plugin import MyPlugin

from mmpy_bot import Bot, Settings


try:
    with open('config.json', 'r', encoding='utf-8') as config:
        # settings = json.loads(config.read())['wiki-search-bot']
        config_settings = json.loads(config.read())

 
except IOError as e:
    print(f'Unable to read config! Reason: {e}')
    sys.exit(1)


def set_settings(Configuration_settings_class, config):
    
    # config['SCHEME'] = Configuration_settings_class.SCHEME
    # for key_annotation in Configuration_settings_class.__annotations__:
    config["SCHEME"] = "http"
    config["SSL_VERIFY"] = False

    for key_config in config:
        # if(key_annotation == key_config):
            # print(config[key_config])
            setattr(Configuration_settings_class,key_config, config[key_config] )
            
            # example_settings.__annotations__[key_annotation] = config[key_config]
    example = config_settings
    return Configuration_settings_class
# set_settings(Settings, config_settings) 
# settings=set_settings(Settings(), config_settings)
# bot = Bot(settings=set_settings(Settings(), config_settings), plugins=[MyPlugin()])





   

bot = Bot(settings=Settings(
        MATTERMOST_URL=config_settings["MATTERMOST_URL"],
        MATTERMOST_PORT=config_settings["MATTERMOST_PORT"],
        MATTERMOST_API_PATH=config_settings["MATTERMOST_API_PATH"],
        BOT_TOKEN=config_settings["BOT_TOKEN"],
        BOT_TEAM=config_settings["BOT_TEAM"],
        SSL_VERIFY=True,
        WEBHOOK_HOST_ENABLED=True,
        SCHEME=False
        # WEBHOOK_HOST_URL=settings['webhook_host'],
        # WEBHOOK_HOST_PORT=settings['webhook_self_port'],
    ),plugins=[MyPlugin()])



bot.run()


# bot = Bot(settings=Settings(
#         MATTERMOST_URL=config_settings["MATTERMOST_URL"],
#         MATTERMOST_PORT=config_settings["MATTERMOST_PORT"],
#         MATTERMOST_API_PATH=config_settings["MATTERMOST_API_PATH"],
#         BOT_TOKEN=config_settings["BOT_TOKEN"],
#         BOT_TEAM=config_settings["BOT_TEAM"],
#         SSL_VERIFY=False,
#         WEBHOOK_HOST_ENABLED=True,
#         # WEBHOOK_HOST_URL=settings['webhook_host'],
#         # WEBHOOK_HOST_PORT=settings['webhook_self_port'],
#     ), plugins=[MyPlugin()])

# bot.run()