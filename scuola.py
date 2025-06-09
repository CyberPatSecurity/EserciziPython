class Persona:
    """Classe per la creazione delle istanze di oggetto persona"""
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età


    def informazioni(self):
        print(f"Nome: {self.nome}, Età: {self.età}")



class Studente(Persona):
    def __init__(self, nome, età, voti):
        super().__init__(nome, età)
        self.voti = voti


    def media_voti(self):
        n = 0
        for elementi in self.voti:
            n += 1
        self.media = sum(self.voti) / n
        return self.media
        
    
    def informazioni(self):
        print(f"Nome: {self.nome}, Età: {self.età}, Media Voti: {self.media}")
        
    
class Professore(Persona):
    def __init__(self,nome, età, materia):
        super().__init__(nome, età)
        self.materia = materia
        



    def assegna_voto(self, studente, voto):
        self.voto = voto
        self.studente = Studente( nome, età, voti)
        self.voti = Studente.voti()    
        print(f"{self.voti}")


    #def informazioni(self):
    #    print(f"Nome: {self.nome}, Età: {self.età} {self.materia} {self.voto}")
        



studente = Studente("Lorenzo", 0, [7, 10, 5, 10])
studente.media_voti()
studente.informazioni()
""""""
voto_prof = Professore("Lorenzo", 0, "Matematica")
voto_prof.assegna_voto(studente, 9)
