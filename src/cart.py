class Cart:
    def __init__(self):
        self._items = {}

    def add_item(self, product_id, price, quantity=1):
        if product_id in self._items:
            self._items[product_id]["quantity"] += quantity
        else:
            self._items[product_id] = {"price": price, "quantity": quantity}

    def remove_item(self, product_id):
        self._items.pop(product_id, None)

    def total(self):
        return sum(item["price"] * item["quantity"] for item in self._items.values())

    @property
    def items(self):
        return dict(self._items)
