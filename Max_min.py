#Scrivere un programma che chiede all'utente di inserire una lista 
#di numeri e restituisce il valore massimo e minimo della lista.

lista_numeri = input("Inserire una lista di numeri separati da uno spazio: ")

numeri_in_lista = [int(numero) for numero in lista_numeri.split()]
valore_massimo = max(numeri_in_lista)
valore_minimo = min(numeri_in_lista)

print(f"il valore massimo della lista è {valore_massimo} mentre il valore minimo è {valore_minimo}")
    