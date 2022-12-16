import requests

from config import *

class FakeUser:
    def __init__(self, username, password, email, name, clearanceLevel):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.clearanceLevel = clearanceLevel
    
    def register(self):
        payload = {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "fullname" : self.name,
            "clearanceLevel": self.clearanceLevel
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
        response_payload = response.json()
        print(response_payload)

          # Set unique session signature
        self.signature = response_payload["data"]["signature"]
        self.id = str(response_payload["data"]["id"])
    
    def get_documents(self):
        response = requests.get(DOCS_ENDPOINT)
        print(response)
        print("get_documents", response.json())


