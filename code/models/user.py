from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def create_user(cls, data):
        user = UserModel.query.filter_by(username=data['username']).first()

        if user:
            return {'message': 'Username {} already exists in database.'.format(data['username'])}, 400
        else:
            user = UserModel(**data)
            try:
                user.save()
            except:
                return {'message': 'An error occurred while saving saving user.'}, 500

            return {'message': 'User created successfully.'}, 201

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
