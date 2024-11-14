import json

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @classmethod
    def load_products(cls, filepath='products.json'):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
            return [cls(**prod) for prod in data]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_products(cls, products, filepath='products.json'):
        with open(filepath, 'w') as file:
            json.dump([prod.__dict__ for prod in products], file)
