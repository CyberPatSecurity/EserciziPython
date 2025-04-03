class Auto:
    """Classe che difinisce un prototipo di macchine"""

    def __init__(self, colore, targa):
        self.colore = colore
        self.targa = targa
        self.carburante = 0
        self.x = 0

    def __del__(self):
        print("Bye")

    def __str__(self):
        return f"[{self.colore} {self.targa} - X: {self.x} - f: {self.carburante}]"

    def addCarburante(self):
        self.carburante += 1
        if self.carburante > 10:
            self.carburante = 10

    def marcia(self):
        if self.carburante > 0:
            self.x += 1
            self.carburante -= 1
            return True
        else:
            return False


a1 = Auto("FN364AW", "Gialla")

for i in range(10):
    a1.addCarburante()

print(a1)
print("partenza")

while a1.marcia():
    print(a1)