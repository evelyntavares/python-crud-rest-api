from db import db


class ProductModel(db.Model):

    sku = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))
    # inventory = db.relationship('InventoryModel')

    def __init__(self, sku, name):
        self.sku = sku
        self.name = name
        # self.inventory_id = inventory_id

    def json(self):
        return {'sku': self.sku, 'name': self.name}

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
            product = ProductModel(sku, data['name'])
            product.save()
            return product.json(), 201

    @classmethod
    def update_product(cls, sku, data):
        product = cls.query.filter_by(sku=sku).first()
        if product:
            product.name = data['name']
        else:
            product = ProductModel(sku, **data)

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
            return  {'message': 'Product deleted sucessfully.'}, 200
        else:
            return {'message': 'No product with sku {} was found to be deleted.'.format(sku)}, 404

