from mmpy_bot import Plugin,Message,  listen_to

import json

from interactive_button import interactive_button_constructor

# with open('./message_button.json', 'r') as msg_btn:
#     msg = json.loads(msg_btn.read())

description = {
    'pretext': 'Привет',
    'text': 'Можно доавить в админы'
}
integration = interactive_button_constructor.integration_structure('http://192.168.88.252:8000/add_admin', 'do_something_update')
integration2 = interactive_button_constructor.integration_structure('http://192.168.88.252:8000/create_user', 'do_something_update')

# button = interactive_button_constructor.button(description, 'message','message',integration)
button2 = interactive_button_constructor.button(description, 'message','create user',integration2)


msg =interactive_button_constructor.attachments(button2)

class MyPlugin(Plugin):
    @listen_to('start')
    
    async def wakeup(self, message:Message):
        self.driver.create_post('yz56g3q71irgdcr8si14wyp14y','123',props=msg)
