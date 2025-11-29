class Empleado:  # clase padre
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_bono(self):
        return 0

class Gerente(Empleado):  # clase hija
    def calcular_bono(self):
        return self.salario * 0.20

class Tecnico(Empleado):  # clase hija
    def calcular_bono(self):
        return self.salario * 0.10


# ejecutar
gerente = Gerente("Ana", 50000)
tecnico = Tecnico("Luis", 30000)

print(f"Gerente Bono: {gerente.calcular_bono()}")
print(f"Técnico Bono: {tecnico.calcular_bono()}")
