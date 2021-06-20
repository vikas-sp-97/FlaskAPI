from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

book_items=[]

class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field is mandatory!')
    parser.add_argument('Author', type=str, required=True, help='This field is mandatory!')
    parser.add_argument('Pages', type=int, required=False)

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, book_items), None)
        if item:
            return item, 200
        else:
            return {"item": None}, 404

    def post(self, name):
        item = next(filter(lambda x: x['name'] == name, book_items), None)
        if item:
            return {"message": f"Book with name {item['name']} already present"}, 400

        data = Book.parser.parse_args()
        book_items.append(data)
        return data, 201

    def delete(self, name):
        pass

    def put(self, name):

        data = Book.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, book_items), None)

        if item is None:
            item = {"name": name, "Author": data['Author'], "Pages": data['Pages']}
            book_items.append(item)
            return {"message": f"Inserted items {item}"}
        else:
            item.update(data)
            return {"message": f"Updated items {item}"}


class GetAllBooks(Resource):

    def get(self):
        return {"books": book_items}