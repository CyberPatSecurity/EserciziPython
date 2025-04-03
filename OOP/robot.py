class Robot:
    """Classe per la creazioni di nuovi robot per la pulizia della casa"""

    def __init__(self, name, prezzo, autonomia):
        self.name = name
        self.prezzo = prezzo
        self.autonomia = autonomia
        self.marca = "Tineco Floor"
        self.caratteristica = "Autopulente - pulizia del rullo automatica"
        self.tecnologia = "NO" if self.name == "Floor One S5" else "YES"
        
    
    def riassunto(self):
        """stampa un sunto delle caratteristiche del robot"""
        print("\nStampa caratteristiche :" )
        print(f"\t Modello : {self.name}")
        print(f"\t marca : {self.marca}.")
        print(f"\t caratteristica pulizia : {self.caratteristica}.")
        print(f"\t prezzo : {self.prezzo} euro.")
        print(f"\t autonomia batteria :{self.autonomia} minuti.")
        print(f"\tTecnologia iloop : {self.tecnologia}\n ")

#creazione degli oggetti dalla classe Robot

Tineco_FLOOR_ONE_S5 = Robot("Floor One S5", 269, 50)
Tineco_iFloor5 = Robot("Floor 5 Breeze", 199, 35)

#---------------------------------------------------#

#----------------------------------------------------#
#chiama funzuione per riassumere le carateristiche 

Tineco_FLOOR_ONE_S5.riassunto()
Tineco_iFloor5.riassunto()

