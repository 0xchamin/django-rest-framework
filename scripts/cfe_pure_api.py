import requests
import json

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    #print(type(json.dumps(data)))
    for obj in data:
        #print(obj['id'])
        if obj['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return r.json()

print(get_list());
#get_list()

def create_update():
    new_data = {
        'user': 1#,
        #'content': ""
    }
    r = requests.post(BASE_URL + ENDPOINT , data=new_data)
    print(r.headers)
    print(r.status_code)
    #print(r.json())
    if r.status_code in range(200, 300):
        #print("***")
        print(r.json())
        return r.json()
    return r.text

#create_update()
