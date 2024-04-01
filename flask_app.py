from flask import Flask
from dotenv import dotenv_values
import requests
import json

config = dotenv_values(".env")
app  = Flask(__name__)


with open('./message_button.json', 'r') as msg_btn:
    msg = json.loads(msg_btn.read())



    





def incoming_webhook(url_webhook, body, headers):
    response = requests.post(url_webhook, body, headers)
    




@app.route('/start_callback',methods=["POST"])
def event_handler_button():
    # print(request.get_json())
    responsed = requests.post('http://10.11.4.230:8065/hooks/hizg6y9ww7yf3bhhu83nyzkzzh',json.dumps(msg), headers={"Content-Type": "application/json"})
    print(responsed.content)
    return "ok"

@app.route('/')
def start_page():
    
    return "<h1>Start Page</h1>"


app.run(config["HOST"], config["PORT"], debug=True)