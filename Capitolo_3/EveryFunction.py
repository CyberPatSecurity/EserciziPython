city = ['Roma', 'Milano', 'Firenze', 'Napoli','Bari']
print(city)
print(city[3])
print(city[-1])
city.append('Livorno')
print(city)
city.insert(1, 'Bologna')
print(city)
del city[1]
print(city)
popped_city = city.pop()
print(city)
print(popped_city)
last_city = city.pop(1)
print(f"The last city i visited in italy is {last_city.title()}")
print(city)
city_remove = 'Roma'
city.remove(city_remove)
print(city)
print(f"\nI removed {city_remove} from the list")
city.append('Roma')
print(city)
city.sort()
print("the original list:")
city.sort(reverse=True)
print(city)
print("\nHere the sorted list:")
print(sorted(city))
print("\nHere the original list again:")
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
lenght = len(city)
print(f"la lista è composta da {lenght} elementi")