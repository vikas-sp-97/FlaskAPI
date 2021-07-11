import yaml
from bookItemsApi.models.userModel import UserModel
from flask_bcrypt import check_password_hash


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    print(user.password)
    if user and check_password_hash(user.password, password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


def get_secret_key():
    with open('/Users/vikassp/PycharmProjects/FlaskAPI/bookitemsApi/config/data.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data['secret_key']


