#Creare una tupla di numeri interi e verificare se tutti i numeri nella tupla sono pari.

input_utente = input("Inserisci una serie di numeri : ")
input_tupla = tuple(int(num) for num in input_utente.split())

for intero in input_tupla:
    if intero % 2 == 0:
        print(f"Il nunmero {intero} è numero pari")
    else :
        print(f"il numero {intero} è dispari")
