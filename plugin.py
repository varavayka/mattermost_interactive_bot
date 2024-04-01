from mmpy_bot import Plugin,Message,  listen_to

import json
with open('./message_button.json', 'r') as msg_btn:
    msg = json.loads(msg_btn.read())


class MyPlugin(Plugin):
    @listen_to('start')
    
    async def start_message(self, message:Message):
        self.driver.create_post('aagw34tzfin88b3tfw5c9arbnh','123',props=msg)






