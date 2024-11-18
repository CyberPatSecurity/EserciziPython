#Scrivere un programma che chiede all'utente di inserire due liste di numeri e restituisce una nuova 
# lista contenente la somma degli elementi corrispondenti delle due liste.

lista_1 = input("Inserire una lista di numeri :" )
lista_2 = input("Inserire un'altra lista di numeri :" ) 

int_lista1 = [int(numero_1) for numero_1 in lista_1.split()]
int_lista2 = [int(numero_2) for numero_2 in lista_2.split()]

lista_somma = []

for numero_1, numero_2 in zip(int_lista1,int_lista2): 
        valore = numero_1 + numero_2
        #print(valore)    
        lista_somma.append(valore)
        
print(lista_somma)  