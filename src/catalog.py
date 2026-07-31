class Catalog:
    def __init__(self):
        self._products = {}

    def add_product(self, product_id, name, price, stock):
        self._products[product_id] = {"name": name, "price": price, "stock": stock}

    def get_product(self, product_id):
        return self._products.get(product_id)

    def search_by_name(self, query):
        query = query.lower()
        return [p for p in self._products.values() if query in p["name"].lower()]

    def update_stock(self, product_id, quantity):
        product = self._products.get(product_id)
        if product is None:
            raise KeyError(f"Producto no encontrado: {product_id}")
        product["stock"] += quantity
