from flask_jwt import jwt_required
from flask_restful import Resource
from bookItemsApi.models.booksModel import BookItemModel
from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields


class BooksRequestSchema(Schema):
    name = fields.Str(required=True, description="name of book")
    Author = fields.Str(required=True, description="Author's name")
    Pages = fields.Int(description="No.of pages in the book")


class BooksGetResponseSchema(Schema):
    name = fields.Str()
    author = fields.Str()
    pages = fields.Int()

class BooksResponseSchema(Schema):
    message = fields.Str()


@doc(description='access token', params={
            'Authorization': {
                'description': 'Authorization HTTP header with JWT access token',
                'in': 'header',
                'type': 'string',
                'required': True
            }})
class Book(MethodResource, Resource):
    @jwt_required()
    @marshal_with(BooksGetResponseSchema)
    def get(self, name):
        item = BookItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        else:
            return {"item": None}, 404

    @jwt_required()
    @use_kwargs(BooksRequestSchema, location=('json'))
    @marshal_with(BooksResponseSchema)
    def post(self, name, **kwargs):
        if BookItemModel.find_by_name(name):
            return {"message": f"Book with name {name} already present"}, 400

        # data = Book.parser.parse_args()
        data = kwargs
        item = BookItemModel(name, data['Author'], data['Pages'])
        try:
            item.save_to_db()
        except Exception as e:
            return {"message": f"Error while inserting into DB! {e}"}

        return item.json(), 201

    @jwt_required()
    @marshal_with(BooksResponseSchema)
    def delete(self, name):
        item = BookItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Deleted book!"}

    @jwt_required()
    @use_kwargs(BooksRequestSchema, location=('json'))
    @marshal_with(BooksResponseSchema)
    def put(self, name, **kwargs):
        data = kwargs
        item = BookItemModel.find_by_name(data['name'])
    #
        if item is None:
            item = BookItemModel(**data)
        else:
            item.author = data['Anuthor']
            item.pages = data['Pages']
        item.save_to_db()
        return {"message": f"Updated items {item}"}


class GetAllBooksResponseSchema(Schema):
    item = fields.List(fields.Dict)


class GetAllBooks(MethodResource, Resource):
    @marshal_with(GetAllBooksResponseSchema)
    def get(self):
        return {"item": list(map(lambda x: x.json(), BookItemModel.query.all()))}
        # return {"item": [item.json() for item in BookItemModel.query.all()]}
