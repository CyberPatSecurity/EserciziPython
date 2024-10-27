# Scrivere un programma che chiede all'utente di inserire una lista di numeri e
# restituisce una nuova lista contenente solo i numeri dispari.
plain_list = input("Inserire una serie di numeri intervallati da uno spazio: ")
switch_to_number = [int(plain_number) for plain_number in plain_list.split()]
odd_numbers  = []

for number in switch_to_number:
    if number % 2 != 0:
        odd_numbers.append(number)
    
if odd_numbers == []:
    print(f"la lista di numeri dispari è vuota {odd_numbers}")
else:
    print(f"la lista di numeri dispari è la seguente {odd_numbers}")