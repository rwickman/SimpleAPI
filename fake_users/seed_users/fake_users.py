
num_users = 10
fake_users = []
for i in range(num_users):
    user = {}
    user["username"] = f"fake_{i}@foo.com"
    user["password"] = f"temp{i}"
    user["email"] = user["username"]
    user["name"] = f"Fake User {i}"
    fake_users.append(user)

