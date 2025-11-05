class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre # atributo publico
        self.__edad = edad  # atributo privado (name mangling)
        self._ocupacion = "Estudiante"  # atributo protegido

class Cuenta:
    def __init__(self,saldo):
        self.__saldo = saldo 
        
    def get_saldo(self):

        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo

# Crear mi objeto Cuenta
mi_cuenta = Cuenta(100)
mi_cuenta.set_saldo(500)
print(mi_cuenta.get_saldo())
