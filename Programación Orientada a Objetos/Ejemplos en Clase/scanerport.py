import socket

class PortScanner: #Clase para escanear puertos

    def __init__(self, Host, Ports): #Funcion que recibe parametros
        self.host = Host #atributo de la clase
        self.port = Ports #atributo de la clase
        self.open_port = [] #lista para puertos abiertos

    def scan(self):
        print(f"Escaneando puertos en {self.host}...") #Inicializar escaner
        for port in self.port: #Recorrer puertos
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crear socket
            sock.settimeout(1) #Establecer tiempo de espera
            result = sock.connect_ex((self.host, port)) #Intentar conectar
            if result == 0: #Si el puerto esta abierto
                print(f"Puerto {port} está abierto")
                self.open_port.append(port) #Agregar a la lista de puertos abiertos
            sock.close() #Cerrar socket
   

    def report(self):
        if self.open_port: #Si hay puertos abiertos
            print(f"Puertos abiertos en {self.host}:") 
            for port in self.open_port: #Recorrer lista de puertos abiertos
                print(f" - Puerto {port} está abierto")
        else:
            print(f"No se encontraron puertos abiertos en {self.host}.")


host = "scanme.nmap.org" #Host a escanear
ports = [21, 22, 23, 8080, 80, 443, 25] #Lista de puertos a escanear       

#crear objeto y ejecutar escaner
scanner1 = PortScanner(host, ports)
scanner1.scan() #Llamar al metodo scan
scanner1.report() #Llamar al metodo report
