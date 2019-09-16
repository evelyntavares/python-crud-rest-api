from db import db


class  WarehouseModel(db.Model):
    __tablename__ = 'warehouses'

    location = db.Column(db.String(80), primary_key=True)
    quantity = db.Column(db.Integer)
    type = db.Column(db.String(80))

    product_sku = db.Column(db.Integer, db.ForeignKey('products.sku'))
    product = db.relationship('ProductModel')


    def __init__(self, location, quantity, type, product_sku):
        self.location = location
        self.quantity = quantity
        self.type = type
        self.product_sku = product_sku

    def json(self):
        return {'location': self.location, 'quantity': self.quantity, 'type': self.type}
