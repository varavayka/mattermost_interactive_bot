import json
from dotenv import dotenv_values
from mmpy_bot import Bot, Settings

from get_config import get_config_file
from plugin import MyPlugin



mattermost_config_server = dotenv_values('.dotenv_mattermost')
config = get_config_file('config.json')
bot = Bot(settings=Settings(**config), plugins=[MyPlugin()])
bot.run()
