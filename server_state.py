# Web client POST a request for a file
# The (user_id, file request) is added to request mangaer
# Assign the mobile app user to the request
# The mobile app user GET the requested assigned to it from server
# Mobile app user POST request response

# Request will need to be assigned to as approver
# 1. Have a class for Request
#   Contains the request and the approver_id
#   Will also need to create a class for Approver
#       Will have reference to PendingRequest as well
#       Can update PendingRequest with RequestResponse
#       Approver Pending
from enum import Enum
import time

WEB_USER_ID = 1
MOBILE_USER_ID = 0

class RequestStatus(Enum):
    pending =  1
    timeout = 2
    approved = 3
    disapproved = 4

TIMEOUT_THRESHOLD = 30

class ApproverAssigner:    
    def assign_approver(self, user_id, file_id):
        return MOBILE_USER_ID


class RequestManager:
    def __init__(self, approvers, approver_assigner):
        self.requests = {}
        self.approvers = approvers
        self.approver_assigner = approver_assigner

    def get_pending(self, approver_id):
        return self.approvers[approver_id].check_pending()

    def update_status(self, approver_id, user_id, file_id, response):
        self.approvers[approver_id].request_response(user_id, file_id, response)

    def check_request(self, user_id, file_id):
        req_id = (user_id, file_id)
        if req_id in self.requests:
            request = self.requests[req_id]            
            # If pending and less than timeout threshold return pending
            # If still not pending, send back response
            # If pending, but over request time, update as timeout and send back timeout

            if time.time() - request.request_time  < TIMEOUT_THRESHOLD and request.status == RequestStatus.pending:
                return request.status.value
            elif request.status != RequestStatus.pending:
                return request.status.value
            else:
                # This should be handled by the server instead
                request.status = RequestStatus.timeout
                return request.status.value

    def create_request(self, user_id, file_id):
        print("CREATING REQUEST")

        if (user_id, file_id) not in self.requests:
            # Assign an approver

            approver_id = self.approver_assigner.assign_approver(user_id, file_id)
            print("approver_id", approver_id)
            request_time = time.time()
            print("request_time", request_time)
            request = FileRequest(user_id, file_id, request_time, approver_id)

            self.approvers[approver_id].add_request(request)

            self.requests[(user_id, file_id)] = request 
        print("SEDNING BACK REQUEST TIME")
        return self.requests[(user_id, file_id)].request_time


class Approver:
    def __init__(self, approver_id):
        self.approver_id = approver_id
        self.pending_requests = {}
    
    def check_pending(self):
        requests = []
        for request in self.pending_requests.values():
            if request.status == RequestStatus.pending:
                requests.append(request.request_dict())
        
        return requests

    def request_response(self, user_id, file_id, response):
        request = self.pending_requests[(user_id, file_id)]
        if time.time() - request.request_time <= TIMEOUT_THRESHOLD:
            if response == RequestStatus.approved.value:
                request.status = RequestStatus.approved
            else:
                request.status = RequestStatus.disapproved
        else:
            # This should be handled by the server instead
            print("SETTING TIMEOUT")
            request.status = RequestStatus.timeout
    
    def add_request(self, request):
        print("request.user_id", request.user_id, "request.file_id", request.file_id)
        self.pending_requests[(request.user_id, request.file_id)]= request 


class FileRequest:
    def __init__(self, user_id, file_id, request_time, approver_id):
        self.user_id = user_id
        self.file_id = file_id
        self.request_time = request_time
        self.status = RequestStatus.pending
        self.approver_id = approver_id
    
    def request_dict(self):
        return {
            "user_id": self.user_id,
            "file_id": self.file_id,
            "request_time": self.request_time}

