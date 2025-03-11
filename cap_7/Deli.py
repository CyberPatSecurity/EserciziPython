sandwiches_orders = ['Tuna sandwich','cheesburger','smashburger','panino con mortadella']
finished_sandwiches = []

while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f"I made your {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwich has made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()}")