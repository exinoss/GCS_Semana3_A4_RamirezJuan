import unittest

from src.catalog import Catalog


class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = Catalog()
        self.catalog.add_product("p1", "Mouse inalambrico", 25.0, 10)

    def test_get_product_returns_data(self):
        product = self.catalog.get_product("p1")
        self.assertEqual(product["name"], "Mouse inalambrico")

    def test_search_by_name_is_case_insensitive(self):
        results = self.catalog.search_by_name("mouse")
        self.assertEqual(len(results), 1)

    def test_update_stock_changes_quantity(self):
        self.catalog.update_stock("p1", -3)
        self.assertEqual(self.catalog.get_product("p1")["stock"], 7)

    def test_update_stock_raises_for_unknown_product(self):
        with self.assertRaises(KeyError):
            self.catalog.update_stock("unknown", -1)


if __name__ == "__main__":
    unittest.main()
