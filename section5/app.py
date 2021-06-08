import os
import sys

from flask import Flask
from flask_restful import Api

from resources.item import Item

sys.path.append('C:\\Users\\Kaiser\\.virtualenvs\\udemy-automated-software-testing-python-7MNovFjM\\lib\\site-packages\\flask_restful')
print(sys.path)

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
api = Api(app)

api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
