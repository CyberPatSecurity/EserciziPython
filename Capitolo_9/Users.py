class User:
    """create a class for profile users"""
    def __init__(self, first_name, last_name, age, sex, location, permission):
        """Initialize user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.location = location
        self.login_attempets = 0
        self.permission = permission

    def describe_user(self):
        print("\nThe following user have been created and has this attributes:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Location: {self.location}")
        print(f"Privilege: {self.permission}")

    def greet_user(self):
        print(f"Hello! {self.first_name} {self.last_name}")

    
    def increment_login_attempts(self):         
        self.login_attempets +=1


    def reset_login_attempts(self):
        self.login_attempets = 0

    """Represent a special User"""

    def __init__(self, first_name, last_name, age, sex, location,permission):
        """
        Initialize attributes of the parent class
        The initialize attributes specific type of restaurant
        """
        super().__init__(first_name, last_name, age, sex, location,permission)
        self.privileges = Privileges()
        
    
   


