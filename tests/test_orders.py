import unittest

from src.cart import Cart
from src.catalog import Catalog
from src.orders import create_order


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()
        self.catalog.add_product("p1", "Teclado mecanico", 60.0, 5)
        self.cart = Cart()
        self.cart.add_item("p1", 60.0, 2)

    def test_create_order_reduces_stock(self):
        create_order("o1", self.cart, self.catalog, "RF-05")
        self.assertEqual(self.catalog.get_product("p1")["stock"], 3)

    def test_create_order_fails_with_empty_cart(self):
        empty_cart = Cart()
        with self.assertRaises(ValueError):
            create_order("o2", empty_cart, self.catalog, "RF-05")

    def test_create_order_fails_with_insufficient_stock(self):
        self.cart.add_item("p1", 60.0, 10)
        with self.assertRaises(ValueError):
            create_order("o3", self.cart, self.catalog, "RF-05")

    def test_create_order_stores_requirement_ref(self):
        order = create_order("o4", self.cart, self.catalog, "RF-05")
        self.assertEqual(order.requirement_ref, "RF-05")

    def test_create_order_fails_without_requirement_ref(self):
        with self.assertRaises(ValueError):
            create_order("o5", self.cart, self.catalog, "")


if __name__ == "__main__":
    unittest.main()
