responses = {}
polling_acticve = True

while polling_acticve:
    name = input("\nWhat's your name? ")
    response = input("If you could visit one place in the world, where would you go?  ")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)  ")

    if repeat == 'no':
        polling_acticve = False

print("\n---Poll result---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")