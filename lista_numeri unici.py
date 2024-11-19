#Scrivere un programma che chiede all'utente di inserire una lista di numeri
#e restituisce una nuova lista contenente solo i numeri unici (senza ripetizioni).

lista_input= input("Inserire una lista di numeri :" )

int_lista = [int(numero) for numero in lista_input.split()]

no_ripetizione =[]

for num in int_lista:
    if num not in no_ripetizione:
        no_ripetizione.append(num)  

print(no_ripetizione)