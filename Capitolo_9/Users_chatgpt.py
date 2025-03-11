"""A class that can be used to represent a user profile."""

class User:
    """Create a class for profile users"""
    
    def __init__(self, first_name, last_name, age, sex, location):
        """Initialize user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.location = location
        self.login_attempts = 0  # Corretto l'errore di battitura

    def describe_user(self):
        """Print user information"""
        print("\nThe following user has been created with these attributes:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Print a greeting to the user"""
        print(f"Hello! {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        """Increment login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0






