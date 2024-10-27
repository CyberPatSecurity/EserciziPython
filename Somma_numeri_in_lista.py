#Scrivere un programma che chiede all'utente di inserire una lista di numeri
#e restituisce la somma di tutti i numeri nella lista.
#

numeri_plain = input("inserire una serie di numeri intervallati da uno spazio: ")
lista = [int(numero) for numero in numeri_plain.split()]
somma = sum(lista)
print(somma)