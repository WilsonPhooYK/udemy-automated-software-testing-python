from models.store import StoreModel
from tests.unit.unit_base_test import UnitBaseTest

class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')
        
        self.assertEqual(store.name, 'test', 'The name of store does not match after creation.')
        