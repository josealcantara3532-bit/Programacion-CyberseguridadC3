class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad no puede ser negativa.")


persona=Persona("Armando", 27)
print(persona.edad) #Getter

persona.edad = 28 #Setter
print(persona.edad)