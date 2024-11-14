from user import User
from product import Product
from inventory import InventoryManager

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role="Admin")

    @classmethod
    def default_admin(cls):
        # Create a default admin with fixed credentials
        return cls("admin", "admin")

    def edit_user_data(self, users, username, new_data):
        # Prevent modifying the default admin's password
        if username == "admin":
            print("Cannot change default admin's data.")
            return False
        for user in users:
            if user.username == username:
                user.__dict__.update(new_data)
                return True
        return False

    def create_user(self, users, username, password, role):
        new_user = User(username, password, role)
        users.append(new_user)

    def add_product(self, inventory, name, price, stock):
        inventory.add_product(name, price, stock)
        print(f"Product '{name}' added to inventory.")

    def remove_product(self, inventory, product_name):
        inventory.remove_product(product_name)
        print(f"Product '{product_name}' removed from inventory.")
