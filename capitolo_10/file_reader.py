file_path="C:\\Users\\Patrizio\\Desktop\\pi_digits.txt"

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
