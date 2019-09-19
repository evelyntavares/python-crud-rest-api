from flask import Flask
from flask_restful import Api
from resource.product import Product, ProductList
from resource.warehouse import Warehouse, WarehouseList
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# End of Swagger configuration


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Product, '/api/products/<int:sku>')
api.add_resource(ProductList, '/api/products')
api.add_resource(Warehouse, '/api/warehouses/<string:location>')
api.add_resource(WarehouseList, '/api/warehouses')


if __name__ == '__main__':
    # to avoid circular reference
    from db import db
    db.init_app(app)
    app.run(host='0.0.0.0', port=5000, debug=True)
