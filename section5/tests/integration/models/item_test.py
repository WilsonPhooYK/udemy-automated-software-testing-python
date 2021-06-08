from models.item import ItemModel
from tests.basetest import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel("test", 19.99)

            self.assertIsNone(
                ItemModel.find_by_name("test"),
                f"Found an item with name {item.name}, but expected not to,",
            )

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name("test"))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name("test"))
