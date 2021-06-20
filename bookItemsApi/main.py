from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from FlaskAPI.bookItemsApi.security import authenticate, identity, get_secret_key

from FlaskAPI.bookItemsApi.books import Book, GetAllBooks
from FlaskAPI.bookItemsApi.user import userRegistration

app = Flask(__name__)
app.secret_key = get_secret_key()
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Book, '/book/<string:name>')
api.add_resource(GetAllBooks, '/get-all-books-details')
api.add_resource(userRegistration, '/register_user')

app.run(debug=True)
