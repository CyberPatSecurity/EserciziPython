print("Dammmi 2 numeri, e li dividerò per te.\n")
print("Enter 'q to quit.")

while True:
    firtst_number = input("\nFirst number: ")
    if firtst_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(firtst_number) / int(second_number)
    except ZeroDivisionError:
        print("Non puoi dividere un numero per zero!")
    else:
        print(answer)