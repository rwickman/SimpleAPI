import requests
import time
import json

URL = "http://127.0.0.1:5000/get_request/0"
r = requests.get(url = URL)

print("r.status_code", r.status_code)
print("r.text", r.text)
d = json.loads(r.text)
print(d)
if d:
    URL = "http://127.0.0.1:5000/request_response/0"
    for i in d:
        r = requests.post(
            url = URL,
            json={"user_id": d[0]["user_id"], "file_id": d[0]["file_id"], "request_response": 3})


    print("r.status_code", r.status_code)
    print("r.text", r.text)
