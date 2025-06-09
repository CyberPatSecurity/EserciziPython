class Persona:
    """Classe per la creazione delle istanze di oggetto persona"""
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età

    
    def presentati(self):
        """Metodo per la presentazione dell'oggetto persona"""
        print(f"Ciao, sono {self.nome} e ho {self.età} anni")
    

class Studente(Persona):
    def __init__(self, nome, età, matricola):
        super().__init__(nome, età)
        self.matricola = matricola
        

    def presentati(self):
        """Override della funzione prentati specifico per la sottoclasse studente"""
        print(f"Ciao, sono {self.nome}, ho {self.età} anni e la mia matricola è la{self.matricola}")
