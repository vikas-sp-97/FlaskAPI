from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from bookItemsApi.security import authenticate, identity, get_secret_key

from bookItemsApi.resources.books import Book, GetAllBooks
from bookItemsApi.resources.user import userRegistration, DeleteUser
from bookItemsApi.db import db

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Book item Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = get_secret_key()
api = Api(app)

doc = FlaskApiSpec(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(Book, '/book/<string:name>')
api.add_resource(GetAllBooks, '/get-all-books-details')
api.add_resource(userRegistration, '/register_user')
api.add_resource(DeleteUser, '/delete_user/<string:username>')

doc.register(GetAllBooks)
doc.register(Book)

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)
