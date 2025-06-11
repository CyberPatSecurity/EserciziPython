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
        print(f"\nNome studente: {self.nome}, Età: {self.età}, Media Voti: {self.media}\n")
        
    
class Professore(Persona):
    def __init__(self,nome, età, materia):
        super().__init__(nome, età)
        self.materia = materia
        
        
    
    def assegna_voto(self, voto):
        self.voto = voto
        self.studente = persona
        self.nuovo_voto = self.studente.voti
        self.nuovo_voto.append(voto)
        #print(self.nuovo_voto)             
        self.media = self.studente.media_voti()
        


    def informazioni(self):
        print(f"Professora Maria Teresa De Angelis - Materia: {self.materia} -> Nome Studente: {self.nome}, Età: {self.età}, Voto Matematica: {self.voto}\n")
        print(f"\tNuova media complessiva dei voti : {self.media}\n")
      

"""_______________________________________________________________________________________________________________________________________"""   

persona = Studente("Lorenzo Egidi Fancelli", 0, [7, 10, 5, 10])
persona.media_voti()
persona.informazioni()

"""_______________________________________________________________________________________________________________________________________"""

voto_prof = Professore("Lorenzo Egidi Fancelli",0, "Matematica")
voto_prof.assegna_voto(10)
voto_prof.informazioni()



