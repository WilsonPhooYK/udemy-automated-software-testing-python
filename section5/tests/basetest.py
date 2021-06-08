"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and make sure that it is a new, blank database each time.
"""
from unittest import TestCase
from db import db
from app import app


class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test clientS
        self.app = app.test_client()
        self.app_context = app.app_context
        pass
    
    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
