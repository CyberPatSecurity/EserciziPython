from datetime import datetime, time

class PortaElettrica:
    """Classe che definisce attributi e metodi per l'utilizzo di un oggetto porta ingresso A"""

    def __init__(self, stato):
        self.stato = stato
        self.bloccata = False
        self.tentativi_apertura = 0

    def __str__(self):
        return f"\nSituazione a inizio giornata: Stato porta -> {self.stato} <-"

    def getTime(self):
        current_time = datetime.now()
        return current_time.time().strftime('%H:%M')

    def blocca(self):
        current_time = datetime.now().time()

        start_m = time(13, 30, 0)
        end_m = time(14, 30, 0)

        start_n = time(18, 0, 0)
        end_n = time(8, 30, 0)

        if start_m <= current_time <= end_m or current_time >= start_n or current_time <= end_n:
            self.bloccata = True
        else:
            self.bloccata = False

    def apri(self):
        """Prova ad aprire la porta: verifica blocco automatico basato sull'orario"""
        self.blocca()  # aggiorna il valore di self.bloccata in base all'orario corrente

        if self.bloccata:
            self.stato = "CHIUSA"
            print("\u26d4 La porta è bloccata: fuori orario di apertura.")
        else:
            self.tentativi_apertura += 1
            self.stato = "APERTA"
            print(f"\n - La porta_A è stata {self.stato} - ")

    def chiudi(self):
        """Funzione per chiudere la porta"""
        self.stato = "CHIUSA"
        print(f"\n - La porta_A è stata {self.stato} - ")

    def getStatoPorta(self):
        """Rendicontazione di quante volte è stata aperta la porta"""
        return self.tentativi_apertura


porta_A = PortaElettrica("CHIUSA")
print(porta_A)

# Simulazione continua in ascolto
while True:
    comando = input("\nPremi INVIO per aprire la porta oppure 'exit' per uscire: ")
    if comando.lower() == 'exit':
        break
    porta_A.apri()
    porta_A.chiudi()
    print(f"\nIl numero di aperture totali è: {porta_A.getStatoPorta()}")
    print(f"Ora: {porta_A.getTime()}")
    print(f"Porta bloccata? {porta_A.bloccata}")
