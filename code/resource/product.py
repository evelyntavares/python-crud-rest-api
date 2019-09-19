from flask_restful import Resource, reqparse
from models.product import ProductModel
from flask_jwt import jwt_required


class Product(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('sku',
                        type=int,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be empty!"
                        )

    def get(self, sku):
        return ProductModel.find_product(sku)

    @jwt_required()
    def post(self, sku):
        data = Product.parser.parse_args()
        return ProductModel.create_product(sku, data)

    @jwt_required()
    def put(self, sku):
        data = Product.parser.parse_args()
        return ProductModel.update_product(sku, data)

    @jwt_required()
    def delete(self, sku):
        return ProductModel.delete(sku)


class ProductList(Resource):
    def get(self):
        return ProductModel.get_product_list()
