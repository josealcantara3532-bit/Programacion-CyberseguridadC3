class dispositivo: #clase padre
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
    def mostrar_info(self):
        print(f"Dispositivo: {self.nombre}, IP: {self.ip}")

class firewall(dispositivo): #clase hija
    def __init__(self, nombre, ip, fabricante):
        super().__init__(nombre, ip) #llamando al constructor de la clase padre
        self.fabricante = fabricante
    def mostrar_info(self): #sobreescribiendo el metodo de la clase padre
        print (f"Firewall: {self.nombre}, IP: {self.ip}, Fabricante: {self.fabricante}")
        
#ejecutar el codigo
dispositivo1 = dispositivo("swich_core","192.168.10.1") #instancia de la clase padre
firewall1 = firewall("cisco_ASA","192.168.1.1/24","Cisco") #instancia de la clase hija  

dispositivo1.mostrar_info() #llamando al metodo de la clase padre
firewall1.mostrar_info() #llamando al metodo de la clase hija
