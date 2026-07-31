class Order:
    def __init__(self, order_id, items, total, requirement_ref):
        self.order_id = order_id
        self.items = items
        self.total = total
        self.requirement_ref = requirement_ref


def create_order(order_id, cart, catalog, requirement_ref):
    if not requirement_ref:
        raise ValueError("El pedido debe referenciar el requisito que lo origina, segun RF-06")

    if not cart.items:
        raise ValueError("El carrito esta vacio, no se puede crear el pedido")

    for product_id, item in cart.items.items():
        product = catalog.get_product(product_id)
        if product is None:
            raise ValueError(f"Producto no encontrado en el catalogo: {product_id}")
        if product["stock"] < item["quantity"]:
            raise ValueError(f"Stock insuficiente para el producto: {product_id}")

    for product_id, item in cart.items.items():
        catalog.update_stock(product_id, -item["quantity"])

    return Order(order_id, cart.items, cart.total(), requirement_ref)
