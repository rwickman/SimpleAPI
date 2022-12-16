
num_users = 10000
fake_users = []
for i in range(num_users):
    user = {}
    user["username"] = f"fake_{i}@foo.com"
    user["password"] = f"temp{i}"
    user["email"] = user["username"]
    user["name"] = f"Fake User {i}"
    user["clearanceLevel"] = i % 5 + 1
    fake_users.append(user)