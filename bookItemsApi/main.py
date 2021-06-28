from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from bookItemsApi.security import authenticate, identity, get_secret_key

from bookItemsApi.resources.books import Book, GetAllBooks
from bookItemsApi.resources.user import userRegistration
from bookItemsApi.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = get_secret_key()
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Book, '/book/<string:name>')
api.add_resource(GetAllBooks, '/get-all-books-details')
api.add_resource(userRegistration, '/register_user')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
