#Scrivere un programma che chiede all'utente di inserire una lista di parole e restituisce la lunghezza media delle parole nella lista.
Lista_parole = input("Inserire una sequenza di parole :")
lista = Lista_parole.split()
numero_parole = len(lista)
#lista_num = map(int, lista)
somma = 0
for parola in lista:
    lung_parola = len(parola)
    somma += lung_parola    

media = somma / numero_parole   
print(media)