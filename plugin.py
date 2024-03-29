from mmpy_bot import Plugin,Message,  listen_to

import json
with open('./message_button.json', 'r') as msg_btn:
    msg = json.loads(msg_btn.read())


class MyPlugin(Plugin):
    @listen_to('start')
    
    async def start_message(self, message:Message):
        self.driver.create_post('g8i1xzw1yf8obfbzpw9nbudssh','123',props=msg)






