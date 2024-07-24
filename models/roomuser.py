from fireo.models import Model
from fireo.fields import TextField, NumberField, DateTime
import fireo
import json

fireo.connection(from_file="room.json")

class User(Model):
  user_name = TextField()
  # user_surname = TextField()
  # user_gender = TextField()
  # user_birthday = DateTime()
  # user_city = TextField()
  # user_university = TextField()
  # user_job = TextField()
  # user_additional = TextField()