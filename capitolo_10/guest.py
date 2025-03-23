username = input("Hi, What's your name? ")

filename = 'guest.txt'


with open(filename, 'w') as file_object:
    file_object.write(f"The user that has log-in to the AD is {username}.")
