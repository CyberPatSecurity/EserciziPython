#Creare una tupla di numeri interi e ordinare i numeri in ordine inverso.

input_utente = input("Inserire una serie di numeri interi a piacere :   ")

input_in_tupla = tuple(int(num) for num in input_utente.split())
lista = []
for number in input_in_tupla:    
    lista.append(number)

lista.reverse()
print('Questa è la lista di numeri inverita:', lista)


