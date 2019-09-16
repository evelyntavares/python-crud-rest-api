from flask import Flask
from flask_restful import Api
from resource.product import Product, ProductList
from resource.warehouse import Warehouse, WarehouseList


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Product, '/api/product/<int:sku>')
api.add_resource(ProductList, '/api/products')
api.add_resource(Warehouse, '/api/warehouse/<string:location>')
api.add_resource(WarehouseList, '/api/warehouses')


if __name__ == '__main__':
    # to avoid circular reference
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
