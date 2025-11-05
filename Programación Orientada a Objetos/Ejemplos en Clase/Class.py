class profesion:
    def inicializar(self, Titulo, Experiencia, Empresa):
        self.titulo = Titulo
        self.empresa = Experiencia
        self.sueldo = Empresa

    def mostrar(self):
        print(f"Título: {self.titulo}")
        print(f"Experiencia: {self.empresa} años")
        print(f"Sueldo: ${self.sueldo} USD")


class Persona:
    # Constructor de la clase (Atributos o características)
    def inicializar(self, Nombre, Edad, Altura, Peso):
        self.nombre = Nombre
        self.edad = Edad
        self.altura = Altura
        self.peso = Peso

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Altura: {self.altura} m")
        print(f"Peso: {self.peso} lb")

    # Metodo de la clase (Comportamientos o acciones)
    #Crear objeto de la clase Persona

persona1 = Persona()  #crea instancia de la clase persona
persona1.inicializar("Juan", 25, 1.75, 200) #inicializa atributos
persona1.imprimir()  #llama al metodo imprimir para mostrar los atributos   

persona2 = Persona()  #crea otra instancia de la clase persona
persona2.inicializar("Ana", 30, 1.65, 160) #inicializa atributos
persona2.imprimir()  #llama al metodo imprimir para mostrar los atributos


profesion1 = profesion()
profesion1.inicializar("Ingeniero Electronico", 4, 1000)
profesion1.mostrar()

