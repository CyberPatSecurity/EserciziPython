class Libro:
    def __init__ (self, titolo, autore, anno, genere):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere


class Biblioteca:
    def __init__(self, nomeBiblioteca):
        self.nomeBiblioteca = nomeBiblioteca
        self.libri = []

    
    def libri_archiviati(self):
        return self.libri
    
    
    def aggiungi_libro(self, libro):
        self.libri.append(libro)
        
    
    def ottieni_libri_genere(self, genere):
        generi = []        
        for book in self.libri:
            if book.genere == genere:
                generi.append(book)
        return generi
    

    def ottieni_libri_usciti_prima_di(self):
        annoDiPub = []
        for book in self.libri:
            if book.anno < 2000:
                annoDiPub.append(book)
        return annoDiPub


libro1 = Libro("Respiro", "Ted Chiang", 2015, "Fantascienza")
libro2 = Libro("Anna Karenina", "Lev TOlstoj", 1840, "Storico")
libro3 = Libro("It", "Stephen King", 1990, "Horror")
libro4 = Libro("Neuromante", "William Gibson", 1980, "Fantascienza")
libro5 = Libro("Tutti i racconti", "Franz Kafka", 1920, "Grottesco")

mia_biblioteca = Biblioteca("Biblioteca Nazionale")

mia_biblioteca.aggiungi_libro(libro1)
mia_biblioteca.aggiungi_libro(libro2)
mia_biblioteca.aggiungi_libro(libro3)
mia_biblioteca.aggiungi_libro(libro4)
mia_biblioteca.aggiungi_libro(libro5)

mia_biblioteca.ottieni_libri_genere("Horror")



for book in mia_biblioteca.libri:
    print(f"Libro -> Titolo - {book.titolo}, Autore - {book.autore}, Anno di pubblicazione - {book.anno}, Genere - {book.genere}\n")

genere_libro = mia_biblioteca.ottieni_libri_genere("Horror")
for book in genere_libro:
    print(f"Lista dei Libri di {book.genere} : {book.titolo}")

anno = mia_biblioteca.ottieni_libri_usciti_prima_di()
for book in anno:
    print(f"Lista dei Libri usciti prima dell'anno 2000 : {book.titolo}")
