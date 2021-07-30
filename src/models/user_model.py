from src.models.base_model import AttrDict
from src.tests.test_user import user


class UserModel(AttrDict):
    id_: int = '$[id]'
    username: str = '$[username]'
    firstName: str = '$[firstName]'
    lastName: str = '$[lastName]'
    email: str = '$[email]'
    password: str = '$[password]'
    phone: str = '$[phone]'
    userStatus: int = '$[userStatus]'


print()


from base_model import AttrDict


class UserModel(AttrDict):
    pass


user = UserModel()
user.username = 'john_doe'
user.firstName = 'John'
user.lastName = 'Doe'
user.email = 'john_doe@example.com'
user.password = '123456'
user.userStatus = 0


