#Scrivere un programma che chiede all'utente di inserire una lista di parole
# e restituisce una nuova lista contenente solo le parole che iniziano con una lettera specifica (ad esempio, la lettera "a").


# Scrivere un programma che chiede all'utente di inserire una lista di parole
# e restituisce una nuova lista contenente solo le parole che iniziano con una lettera specifica (ad esempio, la lettera "a").

lista_input = input("Inserire una lista di parole: ")

# Dividere le parole in una lista
parole_lista = [parola for parola in lista_input.split()]  # Correzione nella sintassi

lista_a = []

# Controllare se ogni parola inizia con la lettera "a"
for parola in parole_lista:
    if parola[0] == 'a':  # Correzione: manca il ":" alla fine dell'if
        lista_a.append(parola)

# Stampare la lista delle parole che iniziano con "a"
print(lista_a)
