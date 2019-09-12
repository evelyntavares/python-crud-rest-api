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
    def find_by_sku(cls, sku):
        return cls.query.filter_by(sku=sku).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

