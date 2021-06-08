from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel("Test", 10.99)
        with self.assertRaises(TypeError, msg="Constructor should be invalid"):
            item2 = ItemModel("Test")  # type: ignore

        self.assertEqual(
            item.name, "Test", "Name of item does not equal constructor argument."
        )
        self.assertEqual(
            item.price, 10.99, "Price of item does not equal constructor argument."
        )

    def test_item_json(self):
        item = ItemModel("Test", 10.99)
        expected = {"name": "Test", "price": 10.99}

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}".format(
                expected, item.json()
            ),
        )
