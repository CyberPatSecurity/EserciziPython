#Creare due tuple di numeri interi della stessa lunghezza 
# e calcolare la somma dei corrispondenti elementi.

input1_tupla = input("Inserisci una lista di numeri separati da spazi : ")
input2_tupla = input("Inserisci un'altra lista di numeri separati da spazi : ")

tupla1_ex = tuple(int(num) for num in input1_tupla.split())
tupla2_ex = tuple(int(num) for num in input2_tupla.split())

for num1,num2 in zip(tupla1_ex,tupla2_ex):
    somma_indici = num1 + num2
    print(somma_indici)
