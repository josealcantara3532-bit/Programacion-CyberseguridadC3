class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# Crear objeto
rect = Rectangulo(5, 10)
print("Área del rectángulo:", rect.calcular_area())
