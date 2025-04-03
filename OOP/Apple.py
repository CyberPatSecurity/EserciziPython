class Apple:
    """classe per istanziare le mele di Adel"""

    def __init__(self):
        print("istanza")
        self.tipo = "golden"
        self.colore = "rosso"
        self.maturazione = "Avanzato"

apple1 = Apple()
apple2 = Apple()
apple3 = Apple()
apple2.colore = "verde"
apple3.colore = "rosa"
apple2.maturazione = "acerbo"

print(f"la prima mela è di tipo {apple1.tipo}, è di colore {apple1.colore} e lo stato di maturazione è {apple1.maturazione}")
print(f"La seconda mela è di tipo {apple2.tipo}, è di colore {apple2.colore} e lo stato di maturazione è {apple2.maturazione}")
print(f"La terza mela è di tipo {apple3.tipo}, è di colore {apple3.colore} e lo sato di maturazione è {apple3.maturazione} ")   