from typing import Optional
from db import db

Model = db.Model

class ItemModel(Model):
    __tablename__ = 'items'

    id: Optional[int] = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80))
    price: float = db.Column(db.Float(precision=2))

    store_id: int = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name: str, price: float, store_id: int):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name: str):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
