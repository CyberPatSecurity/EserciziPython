class Libro:
    def __init__ (self, titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere


class Biblioteca:
    def __init__(self):
        self.libri = []

    
    def libri_archiviati(self):
        return self.libri
    
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        
    
    def ottieni_libri_genere(self, genere):
        generi = []        
        for book in self.libri:
            if book.genere.lower == genere.lower:
                generi.append(book)
        return generi
    

    def ottieni_libri_usciti_prima_di(self, anno):
        annoDiPub = []
        for book in self.libri:
            if book.anno < anno:
                annoDiPub.append(book)
        return annoDiPub


l1 = Libro("Respiro", "Ted Chiang", 2015, "Fantascienza")
l2 = Libro("Anna Karenina", "Lev TOlstoj", 1840, "Storico")
l3 = Libro("It", "Stephen King", 1990, "Horror")
l4 = Libro("Neuromante", "William Gibson", 1980, "Fantascienza")
l5 = Libro("Tutti i racconti", "Franz Kafka", 1920, "Grottesco")

biblioteca = Biblioteca()

biblioteca.aggiungi_libro(l1)
biblioteca.aggiungi_libro(l2)
biblioteca.aggiungi_libro(l3)
biblioteca.aggiungi_libro(l4)
biblioteca.aggiungi_libro(l5)

biblioteca.ottieni_libri_genere("Horror")


# 1. Tutti i libri archiviati
print("Catalogo completo:")
for libro in biblioteca.libri_archiviati():
    print("  ", libro.titolo)

#Libri di genere Fantascientifico
print("\nLibri di fantascienza: ")
for libro in biblioteca.ottieni_libri_genere("Fantascienza"):
    print(" ", libro.titolo)

print("\nLibri usciti prima del 2000")
for libro in biblioteca.ottieni_libri_usciti_prima_di(2000):
    print(" ", libro.titolo)
