import unittest

from src.cart import Cart


class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()

    def test_add_item_accumulates_quantity(self):
        self.cart.add_item("p1", 25.0, 2)
        self.cart.add_item("p1", 25.0, 3)
        self.assertEqual(self.cart.items["p1"]["quantity"], 5)

    def test_remove_item_deletes_entry(self):
        self.cart.add_item("p1", 25.0, 1)
        self.cart.remove_item("p1")
        self.assertNotIn("p1", self.cart.items)

    def test_total_sums_price_times_quantity(self):
        self.cart.add_item("p1", 25.0, 2)
        self.cart.add_item("p2", 10.0, 1)
        self.assertEqual(self.cart.total(), 60.0)


if __name__ == "__main__":
    unittest.main()
