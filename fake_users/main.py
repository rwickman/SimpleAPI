from fake_approver import FakeApprover
from seed_users.fake_users import fake_users
import time
# user = FakeApprover(
#     fake_users[1]["username"],
#     fake_users[1]["password"],
#     fake_users[1]["email"],
#     fake_users[1]["name"],
#     fake_users[1]["clearanceLevel"]
#     )

# print("REGISTERING")
# user.register()
# print("LOGGING IN ")
# user.login()
# print("REQUEST DOCS")
# # print("REQUESTS", user.get_requests())
# user.get_documents()


users = []
security_levels = [5, 5, 5]

for i in range(0,3):
    user = FakeApprover(
    fake_users[i]["username"],
    fake_users[i]["password"],
    fake_users[i]["email"],
    fake_users[i]["name"],
    security_levels[i])
    user.register()
    user.login()
    users.append(user)
    time.sleep(0.5)

users[0].get_documents()

cur_user = 0
while True:
    approval_requests = users[cur_user].get_requests()
    if len(approval_requests) > 0:
        print("approval_requests", approval_requests)
        users[cur_user].request_response(
            approval_requests[0]["requester_id"],
            approval_requests[0]["document_id"],
            approval_requests[0]["signature"])
        time.sleep(1)
    else:
        print("Nothing to approve.")
    time.sleep(2)
    cur_user = (cur_user + 1) % len(users)
    print("cur_user", cur_user)
