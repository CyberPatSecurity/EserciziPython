class Studente:
    def __init__(self, nome, cognome, eta, sesso):
        self.nome = nome
        self.cognome = cognome 
        self.eta = eta
        self.sesso = sesso

class Universita:
    def __init__(self, nome_classe):
        self.nome_classe = nome_classe
        self.studenti = []


    def aggiungi_studenti(self, studente):
        self.studenti.append(studente)

    
    def ottieni_iscritti_maschi(self):
        maschi = []
        for studente in self.studenti:
            if studente.sesso == "M":
                maschi.append(studente)
        return maschi
    
    def ottieni_iscritti_donne(self):
       femmine = []
       for studente in self.studenti:
           if studente.sesso == "F":
               femmine.append(studente)
       return femmine
              
    def calcola_media_eta_uomini(self):
        lista_media = []
        for studente_m in self.studenti:
            if studente_m.sesso == "M":
                lista_media.append(studente_m.eta)
        
        if len(lista_media) == 0:
            return f"Non ci sono studenti maschi"
        else:
            return sum(lista_media) / len(lista_media)    
        
        





s1 = Studente("Bianca", "Egidi Fancelli", 5, "F")
s2 = Studente("Elena", "Franchi", 6, "F")
s3 = Studente("Angelo", "Rodriguez", 6, "M")
s4 = Studente("Maria Antonietta", "Bottoni", 8, "F")
s5 = Studente("Pietro", "Gollini", 5, "M")

mia_classe = Universita("Prima C")

mia_classe.aggiungi_studenti(s1)
mia_classe.aggiungi_studenti(s2)
mia_classe.aggiungi_studenti(s3)
mia_classe.aggiungi_studenti(s4)
mia_classe.aggiungi_studenti(s5)


maschi = mia_classe.ottieni_iscritti_maschi()
for stud in maschi:
    print(f"Lista dei studenti maschi : {stud.nome} {stud.cognome} - {stud.eta} anni\n")

femmine = mia_classe.ottieni_iscritti_donne()
for stud in femmine:
    print(f"Lista delle studentesse : {stud.nome} {stud.cognome} - {stud.eta} anni")

media_maschi = mia_classe.calcola_media_eta_uomini()
print(media_maschi)
