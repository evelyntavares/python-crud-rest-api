from flask_restful import Resource, reqparse
from models.product import ProductModel


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
        product = ProductModel.find_by_sku(sku)
        if product:
            return product.json()
        else:
            return {'message': 'Product not found'}, 404

    def post(self, sku):
        if ProductModel.find_by_sku(sku):
            return {'message': 'A product with sku {} already exists.'.format(sku)}, 400

        data = Product.parser.parse_args()
        product = ProductModel(**data)

        try:
            product.save()
        except:
            return {'message': 'An error occurred when saving the product'}, 500

        return product.json(), 201

    def put(self, sku):
        product = ProductModel.find_by_sku(sku)
        data = Product.parser.parse_args()

        if product is None:  # no product was found
            product = ProductModel(**data)
        else:
            product.name = data['name']

        product.save()
        return product.json()

    def delete(self, sku):
        product = ProductModel.find_by_sku(sku)
        if product:
            product.delete()

        return {'message': 'Item deleted.'}, 200
