from datetime import datetime

class PortaElettrica:
    """Classe che definisce attributi e metodi per l'utilizzo di un oggetto porta ingresso A"""
   
    def __init__(self, stato):
        self.stato = stato
        self.bloccata = False
        self.tentativi_apertura = 0
       
       
    def __str__(self):
        return f"Situazione a inizio giornata: Stato porta -> {self.stato} <-"
   
    def apri(self):
        """Funzione per aprire la porta e ottenere le variazioni del suo stato"""
        if self.stato == "Chiusa":
            self.tentativi_apertura += 1
            self.stato = "Aperta"        
            print(f"\n - La porta_A è stata {self.stato} - ")
            
   
    def chiudi(self):
        """Funzione per chiudere la porta"""
        self.stato = "Chiusa"
        print(f"\n - La porta_A è stata {self.stato} - ")
   
    def getStatoPorta(self):
        """Rendicontazione di quante volte è stata aperta la porta"""
        return self.tentativi_apertura
   
    def getTime(self):
        current_time = datetime.now()
        return current_time.time().strftime('%H:%M')
       
       
porta_A = PortaElettrica("Chiusa")
print(porta_A)
#____________________________________________#

porta_A.apri()
porta_A.chiudi()
#____________________________________________#

porta_A.apri()
porta_A.chiudi()
#____________________________________________#

porta_A.apri()
porta_A.chiudi()
#____________________________________________#



print(f"\nIl numero di apertura della porta al momento è di {porta_A.getStatoPorta()}")

porta_A.getTime()