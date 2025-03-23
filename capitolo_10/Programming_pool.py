filename = 'programming_pool.txt'

print("This program create a poll like for program language!\n")
print("Enter 'quit' if you want to exit fron this program.\n")


while True:
    why_program = input("Why do you like programming? ")

    if why_program.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break # Uscita dal ciclo while

    with open(filename, 'a') as file_object:
        file_object.write(f"{why_program}\n")


