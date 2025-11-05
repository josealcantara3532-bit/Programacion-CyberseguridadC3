class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

    def __str__(self):
        return f"nombre: {self.nombre}, edad = {self.edad}"
    
persona=Persona("Armando", 27)
print(persona)  #Llama al metodo __str__ de la clase Persona
