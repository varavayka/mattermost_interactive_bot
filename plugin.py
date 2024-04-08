from mmpy_bot import Plugin,Message,  listen_to, WebHookEvent, listen_webhook
from dotenv import dotenv_values
import json
import requests
from get_config import get_config_file
import asyncio
from time import sleep
from promise import Promise

from interactive_button_constructor import attachments, button, integration_structure, actions
config = dotenv_values(".env")
desc ={"text": 'Мои Функции: '}

button_list = [
button(desc, 'message', 'officeIT',integration_structure("http://10.11.5.101:8000/info",'do_something_ephemeral')),
button(desc, 'message', 'Стать админом канала',integration_structure("http://10.11.5.101:8000/add_admin_channel",'do_something_ephemeral')),
button(desc, 'message', 'Уровни jira уведомлений',integration_structure("http://10.11.5.101:8000/jira_notification",'do_something_ephemeral')),
# button(desc, 'message', 'officeIT',integration_structure("http://10.11.5.101:8000/info",'do_something_ephemeral')),

]


def test777():
    
   

    sleep(10)
    
    

info_message = attachments(actions(button_list))
# print(info_message)
# print(config['channel_id'])

class MyPlugin(Plugin):

    @listen_to('info1')
    async def info_handler(self, message:Message):
        self.driver.create_post(config['channel_id'],'',props=info_message)
        print('info1')
        # self.driver.direct_message()

    @listen_to('info2')
    async def info_handler2(self, message:Message):
        self.driver.create_post(config['channel_id'],'',props=info_message)
        await asyncio.sleep(10)
        print('info2')
    #     # self.driver.direct_message()
    @listen_to('info3')
    async def info_handler3(self, message:Message):
        self.driver.create_post(config['channel_id'],'',props=info_message)
        # self.driver.direct_message()
        
        
            
        

       

    @listen_webhook('test')
    async def test4(self, event:WebHookEvent):
        # res = requests.post(url='http://10.11.4.230:8065/api/v4/actions/dialogs/open',data=json.dumps(get_config_file('interactive_dalog.json')),headers={"Authorization": "Bearer 67dypsj7q3dg8xj4bymiwmse1a"}  )
        # self.driver.create_post(config['channel_id'],'',props=res)
        print(event.body)
    
   







