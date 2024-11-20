#Scrivere un programma che chiede all'utente di inserire una lista di numeri e restituisce una nuova lista contenente i numeri in ordine inverso.

lista_input = input("Inserire un alista di numeri : ")

int_lista = [int(numero) for numero in lista_input.split()]

int_lista.reverse()

print(int_lista)

