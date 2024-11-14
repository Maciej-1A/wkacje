from admin import Admin
from employee import Employee
from user import User
from inventory import InventoryManager

def main():
    users = User.load_users()
    inventory = InventoryManager()

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "admin":
        admin = Admin.default_admin()
        print("Logged in as Default Admin.")
        
        while True:
            print("\nAdmin Options:")
            print("1. Add User")
            print("2. Edit User")
            print("3. Add Product")
            print("4. Remove Product")
            print("5. View Products")
            print("6. Logout")

            choice = input("Enter choice: ")
            if choice == "1":
                username = input("Enter new users username: ")
                password = input("Enter new users password: ")
                role = input("Enter new user's role (Admin/Employee): ")
                admin.create_user(users, username, password, role)
                User.save_users(users)
            elif choice == "2":
                username = input("Enter the username to edit: ")
                new_password = input("Enter new password: ")
                role = input("Enter new role (Admin/Employee): ")
                new_data = {}
                if new_password:
                    new_data['password'] = new_password
                if role:
                    new_data['role'] = role
                success = admin.edit_user_data(users, username, new_data)
                if success:
                    User.save_users(users)
                    print("User updated successfully.")
                else:
                    print("User not found or cannot edit default admin.")
            elif choice == "3":
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                stock = int(input("Enter product stock quantity: "))
                admin.add_product(inventory, name, price, stock)
            elif choice == "4":
                product_name = input("Enter product name to remove: ")
                admin.remove_product(inventory, product_name)
            elif choice == "5":
                for product in inventory.products:
                    print(f"Product: {product.name}, Stock: {product.stock}, Price: {product.price}")
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
        return

    user = next((u for u in users if u.username == username and u.authenticate(password)), None)

    if user:
        if user.role == "Admin":
            admin = Admin(user.username, user.password)
            print("Logged in as Admin.")
        elif user.role == "Employee":
            employee = Employee(user.username, user.password)
            print("Logged in as Employee.")
            for product in inventory.products:
                print(f"Product: {product.name}, Stock: {product.stock}, Price: {product.price}")
            choice = input("Do you want to place an order? (yes/no): ")
            if choice.lower() == "yes":
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                product = next((p for p in inventory.products if p.name == product_name), None)
                if product:
                    employee.place_order(product, quantity)
                    inventory.save_inventory()
                else:
                    print("Product not found.")
    else:
        print("Invalid credentials.")

if __name__ == "__main__":
    main()
