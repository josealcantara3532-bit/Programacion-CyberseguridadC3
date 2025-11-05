class Empleado:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo del empleado: "))

    def mostrar_datos(self):
        print(f"\nEmpleado: {self.nombre}")
        print(f"\nSueldo: ${self.sueldo} USD")

    def impuesto(self):
        if self.sueldo > 1500:
            print(f"\n{self.nombre} debe pagar impuesto.")
        
        else:
           print(f"\n{self.nombre} no debe pagar impuesto.")
        
   #bloque principal del programa
empleado1 = Empleado()
empleado1.mostrar_datos()
empleado1.impuesto()
