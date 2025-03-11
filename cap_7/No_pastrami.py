sandwiches_orders = ['Tuna sandwich','pastrami','cheesburger','pastrami','smashburger','panino con mortadella','pastrami']

print("\nThe Deli has run out of pastrami, only from the following sandwiches you can choose : ")
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')
print(sandwiches_orders)

finished_sandwiches = []

while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f"\nI made your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwich has made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")