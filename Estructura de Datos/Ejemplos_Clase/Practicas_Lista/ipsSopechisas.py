#Detencion basica de IPs sospechosos
#SIEM, IDS, IPS ICMP -t

ips_detectadas = ["192.168.1.10","10.0.0.5","8.8.8.8","185.220.101.4","45.83.64.1"] #Lista pata almacenar las IPs sospechosas

#Lista de IPs consideradas sospechosas o maliciosas (Blacklist)

ips_maliciosas = ["185.220.101.4","45.83.64.1","123.456.78.9",]

ips_sopechosas = []  #Lista para almacenar las ips que se detecten como sospechosas

for ip in ips_detectadas: #Recorrer la lista de ips detectadas
    if ip in ips_maliciosas: #Verificar si la ip detectada entá en la lista de ips maliciosas
        ips_sopechosas.append(ip) #Agregar la ip sospechosas a la lista

#Mostrar las IPs sospechosas detectadas
print("IPs sospechosas detectadas")
