import os
from typing import Any

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'wilson123'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


@jwt.jwt_error_handler
def auth_error_handler(err: Any) -> Any:
    print(err)
    return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
