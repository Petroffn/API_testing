from src.models.base_model import AttrDict


class UserModel(AttrDict):
    pass


user = UserModel()
user.username = 'john_doe'
user.firstName = 'John'
user.lastName = 'Doe'
user.email = 'john_doe@example.com'
user.password = '123456'
user.userStatus = 0

user_json_path = UserModel
