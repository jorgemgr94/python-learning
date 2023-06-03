# == Regular class ============================

class User:
  # Class attributes
  role = None

  """
    NOTE: Override the __new__() method if you want to tweak the object at creation time.
  """
  def __new__(cls, name):
      print(f'Creating a new {cls.__name__} object: {name}')
      obj = object.__new__(cls)

      obj.name = name.upper()

      print(obj.name)
      return obj

  def __init__(self, name):
      print(f'Initializing the person object...')
      # Instance attributes
      # self.name = name


  # Class method
  @classmethod
  def isAdmin(self):
    return self.role == "admin"

  # Static method
  @staticmethod
  def pi():
    return 3.1416

  # custom string representation of the object
  def __str__(self):
    return f'User name is {self.name}'

  # custom representation of the object
  def __repr__(self):
      return f'User(name = {self.name})'

user = User("Jorge")

print(user.__str__())
print(user.__repr__())
print(user.role)
print("===============================")

# == Child class ==============================
class AdminUser(User):
  role = "admin"

adminUser = AdminUser("Jorge Admin")

print(adminUser.__repr__())
print(adminUser.role)
print("===============================")

# delete an instance property
# del adminUser.role

# delete an instance
del adminUser

# ======================================

