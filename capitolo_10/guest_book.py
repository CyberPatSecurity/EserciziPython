filename = 'guest_book.txt'

print("Enter 'quit' to exit the program")

while True:
    username = input("What's your name? ")
    
    if username.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break # Uscire dal ciclo
    
    print(f"Hello {username}, welcome to my program!")
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{username} has registered.\n")