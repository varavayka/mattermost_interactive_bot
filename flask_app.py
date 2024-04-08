from flask import Flask
from dotenv import dotenv_values
import requests
import json
from get_config import get_config_file

config = dotenv_values(".env")
app  = Flask(__name__)

headers = {
    "Content-Type": "application/json"
}

message_info = {'text': "Работает"}


body = json.dumps(message_info)

    
@app.route('/info',methods=["POST"])
def info_handler():
    response = requests.post(url=f"{config['hook_url']}{config['hook_token']}",data=body, headers=headers)
    print(response.content)
    return response.status_code

@app.route('/add_admin_channel', methods=['POST'])
def add_admin_channel_handler():
    # response = 
    response = requests.post(url=f"{config['hook_url']}{config['hook_token']}/test",data=body, headers=headers)
    print(response)
    # response = requests.post('http://10.11.4.230:8065/api/v4/actions/dialogs/open',)
    # response = requests.put(url=f"{config['hook_url']}{config['hook_token']}",data=body, headers=headers)
    # print(response.content)
    return '200'
    

@app.route('/jira_notification', methods=['POST'])
def jira_notification_handler():
    response = requests.put(url=f"{config['hook_url']}{config['hook_token']}",data=body, headers=headers)
    print(response.content)
    return response.status_code




app.run(config["HOST"], config["PORT"], debug=True)