class User:
    def __init__(self, username):
        self.username = username
        self__password = None

    def set_password(self, password):
        if len(password) >= 6:
            self.__password = password
            print("Password set successfully...")
        else:
            print("Password must be at least 6 characters")
        
        
    def validate_password(self, password):
        if self.__password == password:
            print("Login successful")
            return True
        else:
            print("Invalid password")
            return False
    
user1 = User("syam")

user1.set_password("abc")        # too short
user1.set_password("secret123")  # valid password

user1.validate_password("test123")
user1.validate_password("secret123")
