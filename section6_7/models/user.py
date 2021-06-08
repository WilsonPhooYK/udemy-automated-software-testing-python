from db import db

Model = db.Model
class UserModel(Model):
    __tablname__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String())
    
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_by_username(cls, username: str):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()
