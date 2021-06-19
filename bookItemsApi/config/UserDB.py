import sqlite3

class UserDBSqlLiteTable:

    def __init__(self):
        self.connection = sqlite3.connect('/Users/vikassp/PycharmProjects/flaskApi/FlaskAPI/bookItemsApi/config/data.db')
        self.cursor = self.connection.cursor()

    def create_user_table(self):
        """function to create user table."""
        create_table = "CREATE TABLE user (id int, username text, password text)"
        self.cursor.execute(create_table)

    def insert_value_to_user(self, user):
        """user is a tuple, (id, username, password)"""
        query = "INSERT INTO user VALUES (?,?,?)"
        self.cursor.execute(query, user)
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def get_users(self):
        query = "SELECT * FROM user"
        result = self.cursor.execute(query)
        for row in result:
            print(row)

    def get_user_by_username(self, name):
        query = "select * from user where username = ?"
        result = self.cursor.execute(query, (name,))
        if result:
            return result.fetchone()
        else:
            return None

    def get_user_by_id(self, id):
        query = "select * from user where id = ?"
        result = self.cursor.execute(query, (id,))
        if result:
            return result.fetchone()
        else:
            return None



