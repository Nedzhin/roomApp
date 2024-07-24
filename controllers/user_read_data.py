from models.roomuser import User
import json

def read_data():
  users = User.collection.fetch()
  listuser = []

  for user in users:
    user_dict = { "user_name": user.user_name}
    listuser.append(user_dict)

  user_json = json.dumps(listuser)
  return user_json


