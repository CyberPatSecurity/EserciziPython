#esercizio "seeing the world"
places = ['Londra','Chicago','Mosca','Vienna','Stoccolma']
print("\nHere is the original list: ")
print(places)

print("\nHere is the sorted list: ")
print(sorted(places))

print("\nHere is the original list again: ")
print(places)

print("\nHere is the list in alphabetical reverse order: ")
print(sorted(places,reverse=True))

print("\nHere is the original list again: ")
print(places)

places.reverse()
print("\nHere is the reverse order of the list: ")
print(places)

places.reverse()
print("\nHere is the original list again: ")
print(places)

print("\nHere the list in an alphabetical order")
places.sort()
print(places)

print("\nHere is the list in alphabetical reverse order: ")
places.sort(reverse=True)
print(places)