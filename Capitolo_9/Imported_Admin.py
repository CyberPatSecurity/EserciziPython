from Users_chatgpt import User
from account import Privileges, Admin


my_user = User('Patrizio', 'Egidi', 47, 'M', 'Roma')
my_user.describe_user()
my_user.greet_user()
my_admin = Admin('Patrizio', 'Egidi', 47, 'M', 'Roma')
my_admin.privileges.show_privileges()
