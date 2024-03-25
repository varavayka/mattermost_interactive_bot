import json
import sys
from plugin import MyPlugin

from mmpy_bot import Bot, Settings

# from plugin import SearchPlugin

# try:
#     with open('config.json', 'r', encoding='utf-8') as config:
#         # settings = json.loads(config.read())['wiki-search-bot']
#         settings = json.loads(config.read())

 
# except IOError as e:
#     print(f'Unable to read config! Reason: {e}')
#     sys.exit(1)


bot = Bot(
    settings=Settings(
        MATTERMOST_URL="http://10.11.4.230",
        MATTERMOST_PORT=8065,
        MATTERMOST_API_PATH='/api/v4',
        BOT_TOKEN="44hpfosgtibrdpmyie3anrewbr",
        BOT_TEAM="test",
        SSL_VERIFY=False,
        WEBHOOK_HOST_ENABLED=True,
        # WEBHOOK_HOST_URL=settings['webhook_host'],
        # WEBHOOK_HOST_PORT=settings['webhook_self_port'],
    ),
    plugins=[MyPlugin()],
    # plugins=[SearchPlugin()],
)
bot.run()