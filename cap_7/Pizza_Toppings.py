prompt = "\nPlease, insert the toppings for your pizza: "
prompt += "\n(Enter 'quit' to end you order.) ->  "

while True :
    toppings = input(prompt)
    
    
    if toppings == 'quit':
        break
    else:
        print(f"\nYou'll add {toppings} toppings to your pizza, great!")

    