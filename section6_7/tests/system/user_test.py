from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                # Post as form data
                request = client.post(
                    "/register", data={"username": "test", "password": "1234"}
                )

                self.assertEqual(request.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username("test"))
                self.assertDictEqual(
                    json.loads(request.data), {"message": "User created successfully."}
                )

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                # Post as form data
                client.post("/register", data={"username": "test", "password": "1234"})
                auth_response = client.post(
                    "/auth",
                    data=json.dumps({"username": "test", "password": "1234"}),
                    headers={'Content-Type': 'application/json'}
                )
                
                # {'access_token': 'jasdiaksdhaidiuawiasdaidna'}
                self.assertIn('access_token', json.loads(auth_response.data).keys()) # ['access_token']

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():
                # Post as form data
                client.post("/register", data={"username": "test", "password": "1234"})
                auth_response = client.post("/register", data={"username": "test", "password": "1234"})
                
                self.assertEqual(auth_response.status_code, 400)
                self.assertDictEqual({'message': 'A user with that username already exists'}, json.loads(auth_response.data))
                