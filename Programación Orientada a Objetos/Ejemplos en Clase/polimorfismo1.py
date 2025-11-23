class Empleado:
    def trabajar(self):
        print("El empleado está trabajando.")

class Ingeniero(Empleado):
    def trabajar(self):
        print("El ingeniero está desarrollando software.")

class Tecnico(Empleado):
    def trabajar(self):
        print("El técnico está reparando equipos.")

#Polimorfismo en acción

persona1 = [Empleado(), Ingeniero(), Tecnico()]

for persona in persona1:
    persona.trabajar() #Llama al método trabajar() correspondiente a cada clase