class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento
        print(f"La velocidad ahora es {self.velocidad} km/h")


#Crear objeto
carro = Coche("Hyundai", 80)
carro.aumentar_velocidad(20)
