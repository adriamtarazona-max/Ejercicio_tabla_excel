class Pastas:

    def __init__(self):
        self.coccion = 0

    def hervir(self):
        self.coccion = self.coccion + 20
        print("Nivel de coccion =", self.coccion)

    def listas(self):
        return self.coccion >= 100