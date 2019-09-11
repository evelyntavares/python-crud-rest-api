from flask_restful import Resource, reqparse


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sku',
                        type=int,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('name',
                        type=int,
                        required=True,
                        help="This field cannot be empty!"
                        )

    def get(self, sku):
        pass

    def post(self, sku):
        pass

    def put(self, sku):
        pass

    def delete(self, sku):
        pass

    