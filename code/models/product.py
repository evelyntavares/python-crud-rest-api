from db import db
from models.warehouse import WarehouseModel


class ProductModel(db.Model):
    __tablename__ = 'products'

    sku = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.id'))
    # inventory = db.relationship('InventoryModel')

    warehouses = db.relationship('WarehouseModel', lazy='dynamic')

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name

    def json(self):
        available_quantity = 0
        for warehouse in self.warehouses:
            available_quantity = available_quantity + warehouse.quantity
        return {'sku': self.sku, 'name': self.name,
                'available_quantity': available_quantity,
                'warehouses': [warehouse.json() for warehouse in self.warehouses.all()]}

    @classmethod
    def find_product(cls, sku):
        product = cls.query.filter_by(sku=sku).first()
        if product:
            return product.json()
        else:
            return {'message': 'Product not found'}, 404

    @classmethod
    def create_product(cls, sku, data):
        product = cls.query.filter_by(sku=sku).first()
        if product:
            return {'message': 'Product with sku {} already exists.'.format(sku)}, 400
        else:
            product = ProductModel(**data)
            product.save()
            return product.json(), 201

    @classmethod
    def update_product(cls, sku, data):
        product = cls.query.filter_by(sku=sku).first()
        if product:
            product.name = data['name']
        else:
            product = ProductModel(**data)

        product.save()
        return product.json(), 200

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete(cls, sku):
        product = cls.query.filter_by(sku=sku).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return {'message': 'Product deleted successfully.'}, 200
        else:
            return {'message': 'No product with sku {} was found to be deleted.'.format(sku)}, 404

