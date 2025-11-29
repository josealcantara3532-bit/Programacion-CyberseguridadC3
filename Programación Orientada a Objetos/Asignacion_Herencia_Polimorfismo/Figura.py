import math

class Figura:  # clase padre
    def area(self):
        print("Área general: 0")

class Circulo(Figura):  # hija
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        print(f"Área del círculo: {math.pi * self.radio ** 2}")

class Cuadrado(Figura):  # hija
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        print(f"Área del cuadrado: {self.lado * self.lado}")


# ejecutar
circulo = Circulo(5)
cuadrado = Cuadrado(4)

circulo.area()
cuadrado.area()
