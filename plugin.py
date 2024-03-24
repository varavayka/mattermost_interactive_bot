from mmpy_bot import Plugin,Message,  listen_to

import json
with open('./message_button.json', 'r') as msg_btn:
    msg = json.loads(msg_btn.read())


class MyPlugin(Plugin):
    @listen_to('start')
    
    async def wakeup(self, message:Message):
        self.driver.create_post('ix4bi7cb9bbb8d8jbg9f3snwhy','123',props=msg)







# {
#                 "attachments": [
#                 {
#                     "pretext": "This is the attachment pretext.",
#                     "text": "This is the attachment text.",
#                     "actions": [
#                     {
#                         "id": "message",
#                         "name": "Ephemeral Message",
#                         "integration": {
#                         "url": "http://127.0.0.1:7357",
#                         "context": {
#                             "action": "do_something_ephemeral"
#                         }
#                         }
#                     }, {
#                         "id": "update",
#                         "name": "Update",
#                         "integration": {
#                         "url": "http://127.0.0.1:7357",
#                         "context": {
#                             "action": "do_something_update"
#                         }
#                         }
#                     }
#                     ]
#                 }
#                 ]
#             }
