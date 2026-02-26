from modelo_cocina import Cocina
from modelo_cuchillo import Cuchillo
from modelo_vegetal import Cebolla, Tomate
from modelo_olla import Olla
from modelo_pastas import Pastas


cocina = Cocina(True)

if cocina.verificar_objetos():

    cuchillo = Cuchillo(100)

    cebolla = Cebolla("Cebolla", 100)
    tomate = Tomate("Tomate", 100)

    while cebolla.esta_vivo():
        cuchillo.cortar(cebolla)
        if cuchillo.esta_inutil():
            cuchillo.afilar()

    cebolla.morir()

    while tomate.esta_vivo():
        cuchillo.cortar(tomate)
        if cuchillo.esta_inutil():
            cuchillo.afilar()

    tomate.morir()

    olla = Olla()
    olla.agregar_cebolla()
    olla.agregar_tomate()

    pastas = Pastas()

while not pastas.listas():
    opcion = input("Deseas seguir hirviendo? (si/no): ")

    if opcion == "si":
        pastas.hervir()

        if pastas.listas():
            print("La pasta ha sido servida con exito")
            olla.servir()
            break
    else:
        print("No termino de hervir la pasta. Juego terminado.")
        break