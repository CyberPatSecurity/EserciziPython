class Prodotto:
    def __init__(self, nome, categoria, prezzo, quantita_disponibile):
        self.nome = nome
        self.categoria = categoria
        self.prezzo = prezzo
        self.quantita_disponibile = quantita_disponibile
        
class Negozio:
    def __init__(self):
        self.lista_di_prodotti = []
    
    
    def lista_prodotti_disponibili(self):
        return self.lista_di_prodotti
    
    
    def aggiungi_prodotti(self, prodotto):
        self.lista_di_prodotti.append(prodotto)
        
    
    def acquista(self, articolo):
        for prodotto in self.lista_di_prodotti:
            if prodotto.quantita_disponibile == 0:
                print("\nSpiacente, il prodotto da lei richiesto è terminato")
                break   
            elif articolo not in self.lista_di_prodotti:
                [nome.nome for nome in self.lista_di_prodotti]
                print("Spiacente, il prodotto non è presente nel nostro catalogo")
                
            elif prodotto.nome == articolo:
                prodotto.quantita_disponibile = prodotto.quantita_disponibile - 1
                print(f"\nVenduto l'articolo {prodotto.nome}, quantità disponibile ora: {prodotto.quantita_disponibile}")
                break
                
                
#se 0 il prodotto non è terminato e non deve dare come rilutato -1
#se gomma per esempio il prodotto non è disponibile in catalogo
    
p1 = Prodotto("matita", "cartoleria", 1.0, 10)
p2 = Prodotto("quaderno", "cartoleria", 2.5, 2)
p3 = Prodotto("evidenziatore", "cartoleria", 1.8, 0)

mio_negozio = Negozio()

mio_negozio.aggiungi_prodotti(p1)
mio_negozio.aggiungi_prodotti(p2)
mio_negozio.aggiungi_prodotti(p3)

# Tutti i prodotti disponibili
print("Magazzino Completo: ")
for articolo in mio_negozio.lista_prodotti_disponibili():
    print("  ", articolo.nome)
    
mio_negozio.acquista("evidenziatore")
