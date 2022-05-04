import requests
import time

URL = "http://0.0.0.0:5000/request_file"

r = requests.post(url = URL, json={"user_id": 1, "file_id": 0})

print("r.status_code", r.status_code)
print("r.text", r.text)

time.sleep(2)
r = requests.post(url = URL, json={"user_id": 1, "file_id": 0})
print("r.status_code", r.status_code)
print("r.text", r.text)

time.sleep(2)
r = requests.post(url = URL, json={"user_id": 1, "file_id": 0})
print("r.status_code", r.status_code)
print("r.text", r.text)
