print("\nIl seguente programma esegue l'addizione tra due numeri, prego.\n") 
print("Enter 'q to quit.")
    
while True:
    num_a = input("Scegli il primo addendo: ")        
    if num_a == 'q':
        break
    num_b = input("Scegli il secondo addendo: ")       
    if num_b == 'q':
        break     
    try:
        sum = int(num_a) + int(num_b)  
    
    except ValueError:
        print("Spiacente, non si può eseguire una somma tra due stringhe!")

    else:
        print(f"La somma tra i due numeri è {sum}")

    




