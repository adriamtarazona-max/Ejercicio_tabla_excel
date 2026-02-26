class Cocina:

    def __init__(self, olla):
        self.olla = olla

    def verificar_objetos(self):
        if self.olla == True:
            print("La olla esta lista")
            return True
        else:
            print("No puedes iniciar sin olla")
            return False