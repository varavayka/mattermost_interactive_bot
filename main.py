import json


from mmpy_bot import Bot, Settings, ExamplePlugin, WebHookExample

from plugin import MyPlugin
from get_config import get_config

config = get_config()


bot = Bot(**config, plugins=[MyPlugin()])
# bot.run()