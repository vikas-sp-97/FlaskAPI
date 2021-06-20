from FlaskAPI.bookItemsApi.config.UserDB import UserDBSqlLiteTable
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = UserDBSqlLiteTable()

        result = connection.get_user_by_username(username)
        if result:
            user = cls(*result)

        else:
            user=None

        connection.close_connection()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = UserDBSqlLiteTable()

        result = connection.get_user_by_id(_id)
        if result:
            user = cls(*result)

        else:
            user = None

        connection.close_connection()
        return user


class userRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username field is mandatory!')
    parser.add_argument('password', type=str, required=True, help='Password field is mandatory!')

    def post(self):
        data = userRegistration.parser.parse_args()
        connection = UserDBSqlLiteTable()
        result = connection.insert_value_to_user((data['username'], data['password']))
        print(result)
        connection.close_connection()

