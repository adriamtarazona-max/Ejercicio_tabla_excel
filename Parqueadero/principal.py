from Usuary import Usuario
from car import Carro
from parqueadero import Parqueadero

print ("---sistema parqueadero---")

cedula = input("ingrese su cedula:")
nombre = input("ingrese su nombre:")
tipo_rango = input ("ingrese su tipo de rango:")

usuary = Usuario(cedula,nombre,tipo_rango)

placa = input ("ingrese la placa del carro:")
color = input ("ingrese el color del carro:")
marca = input ("ingrese la maraca del carro:")

carro = Carro (placa,color,marca)

parqueo = Parqueadero(Usuario,carro)

parqueo.registrar_entrada()

opcion = input ("Desea registrar la salida? (si/no)")

if opcion == "si":
    parqueo.registrar_salida()

parqueo.mostrar_info()