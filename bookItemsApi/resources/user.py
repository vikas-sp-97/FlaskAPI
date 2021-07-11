from flask_restful import Resource, reqparse
from bookItemsApi.models.userModel import UserModel


class userRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='username field is mandatory!')
    parser.add_argument('password', type=str, required=True, help='Password field is mandatory!')

    def post(self):
        data = userRegistration.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User already exists in Database!"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": "user inserted"}, 201


class DeleteUser(Resource):

    def delete(self, username):
        user = UserModel.find_by_username(username)
        if user:
            user.delete_from_db()
        return {"message": f"deleted user: {username}"}, 200