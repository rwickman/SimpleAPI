import requests

from fake_user import FakeUser
from config import *

class FakeRequester(FakeUser):
    def __init__(self, username, password, email, name, clearanceLevel):
        super().__init__(username, password, email, name, clearanceLevel)

    def request_access(self, file_id):
        payload = {
            "file_id": file_id,
            "user_id": self.id,
            "signature": self.signature 
        }

        response = requests.post(REQUEST_ACCESS_ENDPOINT, json=payload)
        print(response)
        print(response.json())


requester = FakeRequester(
    username="requester_1",
    password="temp123",
    email="temp@email.com",
    name="Fake  ",
    clearanceLevel=3
)

# requester.register()
# requester.login()
# requester.request_access("62de1ffcc427da0db90800a7")

import asyncio
import websockets
import json


async def hello():
    async with websockets.connect("ws://localhost:4000") as websocket:
        await websocket.send(json.dumps({"type": ""}))
        # await websocket.recv()

asyncio.run(hello())