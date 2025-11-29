class Vehiculo:  # clase padre
    def mover(self):
        print("El vehículo se mueve.")

class Carro(Vehiculo):  # hija
    def mover(self):
        print("El carro avanza usando el motor.")

class Bicicleta(Vehiculo):  # hija
    def mover(self):
        print("La bicicleta avanza al pedalear.")


# ejecutar
vehiculo = Vehiculo()
carro = Carro()
bicicleta = Bicicleta()

vehiculo.mover()
carro.mover()
bicicleta.mover()
