from flask_restful import Resource, reqparse
from models.warehouse import WarehouseModel
from flask_jwt import jwt_required


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

    @jwt_required()
    def post(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.create_warehouse(data)

    @jwt_required()
    def put(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.update_warehouse(data)

    @jwt_required()
    def delete(self, location):
        data = Warehouse.parser.parse_args()
        return WarehouseModel.delete_warehouse(data)


class WarehouseList(Resource):
    def get(self):
        return WarehouseModel.get_warehouse_list()
