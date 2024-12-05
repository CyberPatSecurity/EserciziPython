#Creare una tupla di stringhe e stampare tutte le stringhe che iniziano con una lettera specifica.

input_stringhe = input("Inserire una serie di stringhe : ")

input_tupla = tuple(stringa for stringa in input_stringhe.split())

lettera = 'm'

for stringa_n in input_tupla:
    if stringa_n.startswith(lettera):
        print(stringa_n)
    
    
    
    
    
    
    
    #not in lista_index:
       # lista_index.append(stringa_n)=

#print(lista_index)


#indice_0 = stringa_n[0]
#    if indice_0 not in stringa_n:
#        print(stringa_n)