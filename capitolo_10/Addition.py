def somma_interi(num_a, num_b):
    """esegue la somma di due numeri e testa se i dati in ingresso siano interi con messaggio di errore personalizzato"""  
    
    while True:
        num_a = int(num_a)
        if num_a == 'q':
            break
        num_b = int(num_b)
        if num_b == 'q':
            break     
        try:
            sum = num_a + num_b            
    
        except ValueError:
            print("Spiacente, non si può eseguire una somma tra due stringhe!")
        
        else:
            print(f"La somma tra i due numeri è {sum}")

print("\nIl seguente programma esegue l'addizione tra due numeri, prego.\n")     
print("Enter 'q to quit.")

a = input("Scegli il primo addendo: ")
b = input("Scegli il secondo addendo: ")

somma_interi(a, b)