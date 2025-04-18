def count_words(filename):
    """Count the approximate number of words in a file"""

    try :
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        file_name = 'missing_files.txt'
        with open(file_name, 'a') as file_object:
            file_object.write(filename)
        #print(f"Spiacente, Il file {filename} non esiste!")

    else:        
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
    
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)