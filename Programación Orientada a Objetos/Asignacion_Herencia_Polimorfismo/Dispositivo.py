class Dispositivo:  # padre
    def __init__(self, nombre):
        self.nombre = nombre

    def encender(self):
        print("El dispositivo se está encendiendo.")

class Laptop(Dispositivo):  # hija
    def encender(self):
        print(f"La laptop '{self.nombre}' está iniciando Windows...")

class Telefono(Dispositivo):  # hija
    def encender(self):
        print(f"El teléfono '{self.nombre}' está iniciando Android...")


# ejecutar
laptop1 = Laptop("Lenovo ThinkPad")
tel1 = Telefono("Samsung S22")

laptop1.encender()
tel1.encender()
