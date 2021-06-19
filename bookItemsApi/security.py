from werkzeug.security import safe_str_cmp
import yaml
from FlaskAPI.bookItemsApi.user import User

users = [
    User(1, 'vikas', 'test')
]

user_mapping = {u.username: u for u in users}
user_id_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = user_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id, None)


def get_secret_key():
    with open('/Users/vikassp/PycharmProjects/flaskApi/FlaskAPI/bookitemsApi/config/data.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    return data['secret_key']


