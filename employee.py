from user import User

class Employee(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="Employee")
    
    def place_order(self, product, quantity):
        if product.stock >= quantity:
            product.stock -= quantity
            print(f"Order placed for {quantity} units of {product.name}")
        else:
            print(f"Not enough stock for {product.name}")
