from typing import Any
from models.store import StoreModel
from models.user import UserModel
from models.item import ItemModel
from tests.base_test import BaseTest
from contextlib import contextmanager
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.get_context_client() as client:
            UserModel("test", "1234").save_to_db()
            auth_request = client.post(
                "/auth",
                data=json.dumps({"username": "test", "password": "1234"}),
                headers={"Content-Type": "application/json"},
            )
            auth_token = json.loads(auth_request.data)['access_token']
            self.access_token =  auth_token
    
    @contextmanager
    def get_context_client(self) -> Any:
        with self.app() as client:
            with self.app_context():
                yield client

    def test_get_item_no_auth(self):
        with self.get_context_client() as client:
            resp = client.get("/item/test")

            self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        with self.get_context_client() as client:
            resp = client.get('/item/test', headers={'Authorization': f'JWT {self.access_token}'})
            self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            ItemModel('test', 19.99, 1).save_to_db()
            resp = client.get('/item/test', headers={'Authorization': f'JWT {self.access_token}'})
            self.assertEqual(resp.status_code, 200)

    def test_delete_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            ItemModel('test', 19.99, 1).save_to_db()
            resp = client.delete('/item/test')
            self.assertEqual(resp.status_code, 200)
            self.assertDictEqual({'message': 'Item deleted'}, json.loads(resp.data))

    def test_create_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            
            resp = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
            
            self.assertEqual(resp.status_code, 201)
            self.assertDictEqual({'name': 'test', 'price': 17.99}, json.loads(resp.data))

    def test_create_duplicate_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            ItemModel('test', 17.99, 1).save_to_db()
            
            resp = client.post('/item/test', data={'price': 17.99, 'store_id': 1})
            
            self.assertEqual(resp.status_code, 400)
            self.assertDictEqual({'message': "An item with name 'test' already exists."}, json.loads(resp.data))

    def test_put_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            resp = client.put('/item/test', data={'price': 17.99, 'store_id': 1})
            
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
            self.assertDictEqual({'name': 'test', 'price': 17.99}, json.loads(resp.data))

    def test_put_update_item(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            ItemModel('test', 5.99, 1).save_to_db()
            
            self.assertEqual(ItemModel.find_by_name('test').price, 5.99)
            resp = client.put('/item/test', data={'price': 17.99, 'store_id': 1})
            
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
            self.assertDictEqual({'name': 'test', 'price': 17.99}, json.loads(resp.data))

    def test_item_list(self):
        with self.get_context_client() as client:
            StoreModel('test').save_to_db()
            ItemModel('test', 5.99, 1).save_to_db()
            
            resp = client.get('/items')
            
            self.assertDictEqual({'items': [{'name': 'test', 'price': 5.99}]}, json.loads(resp.data))
            
