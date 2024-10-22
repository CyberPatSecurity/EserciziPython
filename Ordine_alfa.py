#Scrivere un programma che chiede all'utente di inserire una lista
#di parole e restituisce la lista ordinata in ordine alfabetico.
 #
parole = input("Inserire un numero a piacere di parole separati da spazio: ")
lista = parole.split()
lista.sort()
print(lista)
#parole.sort()
#print(parole)