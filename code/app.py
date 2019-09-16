from flask import Flask
from flask_restful import Api
from resource.product import Product


app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Product, '/product/<int:sku>')


if __name__ == '__main__':
    # to avoid circular reference
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
