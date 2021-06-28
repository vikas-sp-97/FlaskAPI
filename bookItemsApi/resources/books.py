from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from bookItemsApi.models.booksModel import BookItemModel


class Book(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field is mandatory!')
    parser.add_argument('Author', type=str, required=True, help='This field is mandatory!')
    parser.add_argument('Pages', type=int, required=False)

    @jwt_required()
    def get(self, name):
        item = BookItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {"item": None}, 404

    def post(self, name):
        if BookItemModel.find_by_name(name):
            return {"message": f"Book with name {name} already present"}, 400

        data = Book.parser.parse_args()
        if data['name'] != name:
            return {"message": f"Miss-match in data submitted {data['name']} and req-params {name}"}, 400
        item = BookItemModel(name, data['Author'], data['Pages'])
        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"Error while inserting into DB! {e}"}

        return item.json(), 201

    def delete(self, name):
        item = BookItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Deleted book!"}

    def put(self, name):
        data = Book.parser.parse_args()
        item = BookItemModel.find_by_name(name)

        if item is None:
            item = BookItemModel(**data)
        else:
            item.author = data['Anuthor']
            item.pages = data['Pages']
        item.save_to_db()
        return {"message": f"Updated items {item}"}


class GetAllBooks(Resource):

    def get(self):
        return {"item": list(map(lambda x: x.json(), BookItemModel.query.all()))}
        # return {"item": [item.json() for item in BookItemModel.query.all()]}