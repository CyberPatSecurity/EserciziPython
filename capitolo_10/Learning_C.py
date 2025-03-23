filename = 'text_files/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    new_language = contents.replace('Python','C')

print("Contenuto del file modificato:\n", new_language)