class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


# crear objeto
est = Estudiante("José", [90, 85, 95])
print("Promedio:", est.calcular_promedio())
