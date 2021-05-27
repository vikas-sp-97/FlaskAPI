from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

book_items = []


class Book(Resource):

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, book_items), None)
        if item:
            return item, 200
        else:
            return {"item": None}, 404

    def post(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, book_items), None)
        if item:
            return {"message": f"Book with name {item['name']} already present"}, 400

        book_items.append(data)
        return data, 201


class GetAllBooks(Resource):

    def get(self):
        return {"books": book_items}


api.add_resource(Book, '/book/<string:name>')
api.add_resource(GetAllBooks, '/get-all-books-details')

app.run(debug=True)
