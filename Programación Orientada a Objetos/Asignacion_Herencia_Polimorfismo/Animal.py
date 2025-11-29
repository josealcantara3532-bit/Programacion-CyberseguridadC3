class Animal:  # clase padre
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):  # clase hija
    def hablar(self):
        print(f"{self.nombre}: ¡Guau guau!")

class Gato(Animal):  # clase hija
    def hablar(self):
        print(f"{self.nombre}: ¡Miau!")


# ejecutar
animal1 = Animal("Animal Genérico")
perro1 = Perro("Bobby")
gato1 = Gato("Misu")

animal1.hablar()
perro1.hablar()
gato1.hablar()
