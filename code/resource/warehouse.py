from flask_restful import Resource, reqparse
from models.warehouse import WarehouseModel


class Warehouse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('type',
                        type=str,
                        required=True,
                        help="This field cannot be empty!"
                        )

    parser.add_argument('product_sku',
                        type=int,
                        required=True,
                        help="This field cannot be empty!"
                        )

    def get(self, location):
        return WarehouseModel.find_warehouse(location)

    def post(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.create_warehouse(data)

    def put(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.update_warehouse(data)

    def delete(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.delete_warehouse(data)


class WarehouseList(Resource):
    def get(self):
        return {'warehouses': [warehouse.json() for warehouse in WarehouseModel.query.all()]}, 200
