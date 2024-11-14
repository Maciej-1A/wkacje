import json

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
    def authenticate(self, password):
        return self.password == password

    @classmethod
    def load_users(cls, filepath='users.json'):
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
            return [cls(**user) for user in data]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_users(cls, users, filepath='users.json'):
        with open(filepath, 'w') as file:
            json.dump([user.__dict__ for user in users], file)
