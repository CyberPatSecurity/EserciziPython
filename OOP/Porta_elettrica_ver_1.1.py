from datetime import datetime

class PortaElettrica:
    """Classe che definisce attributi e metodi per l'utilizzo di un oggetto porta ingresso A"""
   
    def __init__(self, stato,bloccata):
        self.stato = stato
        self.bloccata = bloccata
        self.tentativi_apertura = 0
    
    def __str__(self):
        return f"\nSituazione a inizio giornata: Stato porta -> {self.stato} <-"
    
    def getTime(self):
        current_time = datetime.now()
        return current_time.time().strftime('%H:%M')
    
    def blocca(self):
        current_time = datetime.now().time()
    
        start_m = datetime.time(13, 30, 0)
        end_m = datetime.time(14, 30, 0)
    
        start_n = datetime.time(18, 0, 0)
        end_n = datetime.time(8, 30, 0)
    
        if start_m <= current_time <= end_m or current_time >= start_n or current_time <= end_n:
        self.bloccata = True
        else:
        self.bloccata = False

                

    def apri(self):
        """Funzione per aprire la porta e ottenere le variazioni del suo stato"""
        if self.bloccata == True :
            self.stato = "CHIUSA"
            print(f"La porta nel segeunte orario non può essere aperta")
        else:
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
print(f"\nOra: {porta_A.getTime()}")
print(porta_A(self.bloccata))
