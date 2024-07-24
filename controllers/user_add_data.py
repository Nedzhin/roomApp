from models.roomuser import User


def add_new(**kwargs):
  u = User()

  for key, value in kwargs.items():
    setattr(u, key, value)
  
  u.save()