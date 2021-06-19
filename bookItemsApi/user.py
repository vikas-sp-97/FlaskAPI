import sqlite3
from FlaskAPI.bookItemsApi.config.UserDB import UserDBSqlLiteTable

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
