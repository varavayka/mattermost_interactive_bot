from flask import Flask
from flask import request
import requests
import json
app  = Flask(__name__)

response ={
    "text": "Hello, this is some text\nThis is more text. 🎉"
}

@app.route('/start_callback',methods=["POST"])
def event_handler_button():
    # print(request.get_json())
    responsed = requests.post('http://10.11.4.230:8065/hooks/u9tujs6ud78mtj7naebneftwdy',json.dumps(response), headers={"Content-Type": "application/json"})
    print(responsed.content)
    return "ok"

@app.route('/')
def start_page():
    
    return "<h1>Start Page</h1>"
app.run('10.11.5.101', 8000)