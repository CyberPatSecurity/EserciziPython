number = input("Tell me a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nYour number: {number} is a multiple of 10.")
else:
    print(f"\nYour number isn' a multiple of 10 and 10 isn't divisor of {number}.")