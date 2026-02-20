class Usuario:
    def __init__(self,cedula,nombre,tipo_rango):
        self.cedula = cedula
        self.nombre = nombre
        self.tipo_rango = tipo_rango

    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self,nueva_cedula):
        self.cedula = nueva_cedula

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_tipo_rango(self):
        return self.tipo_rango
    
    def set_tipo_rango(self,nuevo_tipo_rango):
        self.tipo_rango = nuevo_tipo_rango

    def mostrar_info(self):
        print (f"cedula usuario: {self.cedula}")
        print (f"nombre usuario: {self.nombre}")
        print (f"tipo rango: {self.tipo_rango}")
