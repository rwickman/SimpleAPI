import requests
import time

from config import *
from fake_user import FakeUser
from seed_users.fake_users import fake_users


class FakeApprover(FakeUser):
    def __init__(self, username, password, email, name, clearanceLevel):
        super().__init__(username, password, email, name, clearanceLevel)

    def get_requests(self):
        payload = {
            "approver_id": self.id
        }

        response = requests.post(REQUESTS_ENDPOINT, json=payload)

        response_payload = response.json()
        return response_payload["data"]


    def request_response(self, requester_id, file_id, signature):
        payload = {
            "approver_id": self.id,
            "requester_id": requester_id,
            "file_id": file_id,    
            "signature": signature
        }

        requests.post(url=ACCESS_ENDPOINT, json=payload)


# import time


