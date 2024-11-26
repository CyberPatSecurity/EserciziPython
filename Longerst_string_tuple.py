#Creare una tupla di stringhe e stampare la stringa più lunga.

tupla1 = ('pappa','roma','nanna','limone')

lenght_string = []

for stringa in tupla1:
    long_index = len(stringa)
    lenght_string.append(long_index)

valore_massimo = max(lenght_string)
indice_max = lenght_string.index(valore_massimo)

print(tupla1[indice_max])