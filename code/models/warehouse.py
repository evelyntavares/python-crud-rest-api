from db import db


class WarehouseModel(db.Model):
    __tablename__ = 'warehouses'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(80))
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

    @classmethod
    def find_warehouse(cls, location):
        warehouse = cls.query.filter_by(location=location).first()
        if warehouse:
            return warehouse.json()
        else:
            return {'message': 'Warehouse not found.'}, 404

    @classmethod
    def create_warehouse(cls, data):
        warehouse = cls.query.filter_by(location=data['location'], type=data['type']).first()

        if warehouse:
            print(warehouse)
            return {'message': 'A warehouse in {} with type {} already exists in database.'.format(
                data['location'], data['type'])}, 400
        else:
            print(data)
            warehouse = WarehouseModel(**data)

            try:
                warehouse.save()
            except:
                return {'message': 'An error occurred while saving warehouse.'}, 500

            return warehouse.json(), 200

    @classmethod
    def update_warehouse(cls, data):
        warehouse = cls.query.filter_by(location=data['location'], type=data['type']).first()
        if warehouse:
            warehouse.quantity = data['quantity']
        else:
            warehouse = WarehouseModel(**data)

        try:
            warehouse.save()
        except:
            return {'message': 'An error occurred while saving saving warehouse.'}, 500

        return warehouse.json(), 200

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_warehouse(cls, data):
        warehouse = cls.query.filter_by(location=data['location'], type=data['type']).first()
        if warehouse:
            db.session.delete(warehouse)
            db.session.commit()
            return {'message': 'Warehouse deleted successfully.'}, 200
        else:
            return {'message': 'No warehouse in {} with type {} was found to be deleted.'.format(
                location=data['location'], type=data['type'])}, 404

    @classmethod
    def get_warehouse_list(cls):
        return {'warehouses': [warehouse.json() for warehouse in cls.query.all()]}, 200
