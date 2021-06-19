from werkzeug.security import safe_str_cmp
import yaml
from FlaskAPI.bookItemsApi.user import User


def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)


def get_secret_key():
    with open('/Users/vikassp/PycharmProjects/flaskApi/FlaskAPI/bookitemsApi/config/data.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data['secret_key']


