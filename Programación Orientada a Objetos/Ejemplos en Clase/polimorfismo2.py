class Dispositivo_Seguridad:
    def analizar(self):
        print("[Base ] Analizando Sistema...")

class Firewall(Dispositivo_Seguridad):
    def analizar(self):
        print("[Firewall] Analizando tráfico de red...")    

class Antivirus(Dispositivo_Seguridad):
    def analizar(self):
        print("[Antivirus] Escaneando archivos en busca de malware...")

class IDS(Dispositivo_Seguridad):
    def analizar(self):
        print("[IDS] Monitoreando actividades sospechosas en la red...")

# Polimorfismo en acción
dispositivos = [Firewall(), Antivirus(), IDS()]
for dispositivo in dispositivos:
    dispositivo.analizar()  # Llama al método analizar() correspondiente a cada clase   
