glossary_python = {
    'if' : 'Usato per verificare se una condizione sia vera',
    'for' : "Utilizzato per iterare su una lista o un numero di elementi",
    'else' : "Utilizzato quando la condizione if non è vera",
    'list' : "Insieme eterogeneo di elementi detto anche array, modificabile",
    'tuple' : "Insieme eterogeneo di elementi detto anche array, non modificabile",
    'dictionary' : "Insieme di dati che permette di mettere in relazione informazioni tra di loro",
    'boolean' : "Una espressione booleana è un modo di intendere un test condizionale, viene mantenuta per tenere traccia lo stato di un programma o alcune condizioni",
    'range' : "se si vuole ottenere una lista di numeri dati solo il primo e l'ultimo numero, il metodo range ne permette la visualizzazione esempio: list(range(1,6) visualizzaerà i numeri da 1 a n-1",
    'sorted' : "il metodo sorted() mette in ordine alfabetico gli elementi di una lista",
    'and' : "rappresenta l'operatore logico soddisfatto a 1 solose entambe le condizioni sono entrambe vere o a 1",
    'or' : "rappresentazione dell'operatore logico soddisfatto alla verità anche se solo una delle condizioni è vera", 
}
for key,value in glossary_python.items():
    print(f"{key.title()} \n{value}")
