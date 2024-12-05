#Creare una tupla di numeri interi e ordinare i numeri in ordine decrescente.

input_utente = input("Inserire una serie di numeri a piacere:  ")

input_in_tuple = tuple(int(num) for num in input_utente.split())

lista_decrescente = sorted(input_in_tuple, reverse = True)

print('Questa è la lista di numeri decrescenti:', lista_decrescente)