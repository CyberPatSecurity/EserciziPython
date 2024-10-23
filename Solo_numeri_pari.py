#Scrivere un programma che chiede all'utente di inserire una lista di numeri
#  e restituisce una nuova lista contenente solo i numeri pari.
lista_numeri = input("Inserire una lista di numeri separati da uno spazio: ") #input dell'utente

numeri_non_analizzati = [int(numero) for numero in lista_numeri.split()] #trasformazione dell'input utente (in stringa) in valori interi
numeri_pari = []    #lista vuota per contenere i numeri pari


for numero in numeri_non_analizzati:
    if numero % 2 == 0:
        print(f"numero pari verificato: {numero}")
        numeri_pari.append(numero)
    else:
        print(f"numero dispari verificato: {numero}")


print(f"I numeri pari torvati sono: {numeri_pari}")
        


'''
    if numero % 2 == 0:
        numero_corrente = numeri_non_analizzati.pop()

        print(f"numero pari verificato: {numero_corrente}")
        numeri_pari.append(numero_corrente)

print(numeri_pari)
'''