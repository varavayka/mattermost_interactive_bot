import json


from mmpy_bot import Bot, Settings

from plugin import MyPlugin
from get_config import get_config

config = get_config()


bot = Bot(Settings(MATTERMOST_URL = "http://192.168.88.254",
        MATTERMOST_PORT = 8065,
        BOT_TOKEN = "yqzyr3z8kbgypr16yftsntuyqe",
        BOT_TEAM = "dev",
        SSL_VERIFY = True,), plugins=[MyPlugin()])
bot.run()