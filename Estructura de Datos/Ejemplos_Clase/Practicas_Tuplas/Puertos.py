# Definición de una tupla para almacenar puertos abiertos en un servidor
puertos_abiertos = (22, 23, 25, 135, 139, 445, 3389)  # Puertos críticos conocidos

# Lista de conexiones detectadas en el servidor (IP, Puerto)
conexiones_detectadas = [
    ("192.168.1.10", 22),
    ("10.0.0.5", 8080),
    ("172.16.0.3", 445),
    ("192.168.1.12", 443),
    ("192.168.1.20", 3389)
]

# Verificar qué conexiones están utilizando puertos críticos
conexiones_sospechosas = [
    (ip, puerto) for (ip, puerto) in conexiones_detectadas if puerto in puertos_abiertos
]

# Imprimir resultado final
print("Conexiones sospechosas detectadas en puertos críticos:\n")
if len(conexiones_sospechosas) == 0:
    print("No se detectaron conexiones sospechosas.")
else:
    for ip, puerto in conexiones_sospechosas:
        print(f"- IP: {ip} | Puerto: {puerto}")

