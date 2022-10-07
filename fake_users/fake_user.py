import requests

from config import *
from seed_users.fake_users import fake_users

class FakeUser:
    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
    
    def register(self):
        payload = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "fullname" : self.name
        }

        response = requests.post(url=REGISTER_ENDPOINT, json=payload)
        print(response)
        print(response.json())
    
    def login(self):
        payload = {
            "username": self.username,
            "password": self.password,
        }

        response = requests.post(url=LOGIN_ENDPOINT, json=payload)
        print(response)
        print(response.json())
    
    def getRequests(self):
        payload = {
            "username": self.username
        }

        response = requests.get(REQUESTS_ENDPOINT, params=payload)
        print(response)
        print(response.json())
    
    def requestResponse(self, requester_id, file_id, signature):
        payload = {
            "approver_id": self.username,
            "requester_id": requester_id,
            "file_id": file_id,    
            "signature": signature
        }

        requests.post(url=ACCESS_ENDPOINT, json=payload)





user = FakeUser(
    fake_users[0]["username"],
    fake_users[0]["password"],
    fake_users[0]["email"],
    fake_users[0]["name"])
user.login()

