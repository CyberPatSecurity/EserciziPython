#Creare una tupla di numeri interi e verificare se un numero specifico è presente nella tupla..

input_utente = input("inserire una serie di numeri : ")

in_tupla = tuple(int(num) for num in input_utente.split())

input_num = input("ora scegli un numero e ti dirò se è presente nella tupla :")

int_num = int(input_num)

if int_num in in_tupla:
    print(f"Il numero {int_num} è presente nella tupla")
else:   
    print("Il numero non è presente nella tupla")

