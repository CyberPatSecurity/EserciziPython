filename = 'text_files/learning_python.txt'

# Metodo 1: Leggere e stampare tutto il contenuto del file in una volta sola
with open(filename) as file_object:
    contents = file_object.read()
print("Full file content:\n", contents)

# Metodo 2: Leggere e stampare il file riga per riga iterando sull'oggetto file
print("\nReading file line by line:")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Metodo 3: Leggere tutte le righe in una lista e lavorare con esse
with open(filename) as file_object:
    lines = file_object.readlines()

# Unire tutte le righe in una stringa e stampare il contenuto senza interruzioni
python_string = ''.join(line.rstrip() for line in lines)
print("\nContent stored in a single string:\n", python_string)