"""A set of class that can be used to represent an accoun user."""

from Users_chatgpt import User

class Privileges:
    """A separate class to handle Admin privileges"""

    def __init__(self, privileges=None):
        """Initialize privileges"""
        if privileges is None:
            self.privileges = ["Can add post", "Can delete post", "Can ban User", "Can stop a discussion", "Can add another administrator"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Print the privileges"""
        print("\nAn Administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"-- {privilege} --")


class Admin(User):
    """Represent a special type of user: Administrator"""

    def __init__(self, first_name, last_name, age, sex, location):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Admin.
        """
        super().__init__(first_name, last_name, age, sex, location)
        self.privileges = Privileges()  # Create an instance of Privileges class
    """Represent a special User"""
   




