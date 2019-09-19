from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be empty!"
                        )

    def post(self):
        data = User.parser.parse_args()
        return UserModel.create_user(data)
