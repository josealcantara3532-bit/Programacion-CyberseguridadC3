class automovil:
    def __init__(self, marca, modelo, color):
        """Constructor de la clase Automovil"""
        self.marca = marca # atributo
        self.modelo = modelo # atributo
        self.color = color # atributo
        self.velocidad = 0 # atributo

    def acelerar(self, incremento ) :
        """Método para acelerar el automóvil"""
        self.velocidad += incremento
        return(f"El automóvil {self.marca} {self.modelo} está acelerando en {incremento} km/h.")
    
    def frenar(self, decremento):
        """Método para frenar el automóvil"""
        
        if self.velocidad -decremento < 0:
            self.velocidad = 0
        else:
            self.velocidad -= decremento
        return(f"El automóvil {self.marca} {self.modelo} está frenando en {self.velocidad} km/h.")
    
    def tocar_bocina(self):
        """Método para tocar la bocina"""
        return("¡Beep Beep!")
    
    def mostrar_estado(self):
        """Método para mostrar el estado actual del automóvil"""
        return(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h.")
    
# Crear objeto Automovil
Mi_Auto = automovil("Hyundai", "Sonata", "Gris")
Rent_Auto = automovil("Honda", "CRV", "Gris")
print(Mi_Auto.mostrar_estado())

#Acelerar el auto
print(Mi_Auto.acelerar(50))

#Frenar el auto 
print(Mi_Auto.frenar(20))

#Tocar bocina
print(Mi_Auto.tocar_bocina())

#mostrar estado actual
print(Mi_Auto.mostrar_estado())

