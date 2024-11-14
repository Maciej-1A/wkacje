from product import Product

class InventoryManager:
    def __init__(self):
        self.products = Product.load_products()

    def add_product(self, name, price, stock):
        new_product = Product(name, price, stock)
        self.products.append(new_product)
        self.save_inventory()

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]
        self.save_inventory()

    def save_inventory(self):
        Product.save_products(self.products)
