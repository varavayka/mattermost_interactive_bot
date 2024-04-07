import requests
import json
from flask import Flask

app = Flask(__name__)

user_scheme = {
"email": "api_create_user@gmail.com",
"username": "api_create_user",
# "first_name": "zal",
# "last_name": "upa",
"nickname": "api_create_user404",
# "auth_data": "zalupa@gmail.com",
"auth_service": "signup",
"password": "qwerty123",
"locale": "ru",
}
header1= {'Content-Type':'application/json', "Authorization": "Bearer yqzyr3z8kbgypr16yftsntuyqe"}

url = 'http://192.168.88.254:8065'
def add_admin_role(url, channel_id, user_id, body, headers):
    path = f"{url}/api/v4/channels/{channel_id}/members/{user_id}/schemeRoles"
    return requests.put(url=path,data=json.dumps(body), headers=headers)


def create_user(url, body, header):
    path = f"{url}/api/v4/users"
    return requests.post(url=path,data=json.dumps(body), headers=header)

       

# @app.route("/add_admin",methods=['POST'])
# def add_admin_handler():
    
#     response = add_admin_role('http://192.168.88.254:8065',"yz56g3q71irgdcr8si14wyp14y", "7n8bhs8czbd8im7ke6iidpwtue",
#     {"scheme_user": True, "scheme_admin": True},
#     {'Content-Type':'application/json', "Authorization": "Bearer yqzyr3z8kbgypr16yftsntuyqe"})

#     # requests.post('http://192.168.88.254:8065/hooks/9tj99gy1x7r7887u98wguo1xoo', response)
#     print(response.content)
#     # print(response)
#     return "123"

@app.route("/create_user",methods=['POST'])
def create_user1():
    response = create_user(url,user_scheme, header1)

    
    print(response.content)
    # print(response)
    return "123"


   
    


app.run('192.168.88.252', 8000, True)