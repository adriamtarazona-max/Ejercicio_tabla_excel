class Olla:

    def __init__(self):
        self.cebolla = False
        self.tomate = False

    def agregar_cebolla(self):
        self.cebolla = True
        print("Cebolla agregada")

    def agregar_tomate(self):
        self.tomate = True
        print("Tomate agregado")

    def servir(self):
        print("La pasta ha sido servida con exito")