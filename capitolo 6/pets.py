pet_0 = {'kind' : 'dog', 'name_prop' : 'Luisa', 'name_of_pet' : 'Coky'}
pet_1 = {'kind' : 'cat', 'name_prop' : 'Manuela', 'name_of_pet' :'Fluffy'}
pet_2 = {'kind' : 'gallina', 'name_prop' : 'Manuele', 'name_of_pet' :'Guendalina'}
pet_3 = {'kind' : 'dog', 'name_prop' : 'Alessandra', 'name_of_pet' :'Momo'}


pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    print(f"The pet of {pet['name_prop']} is a {pet['kind']} and its name is {pet['name_of_pet']}")