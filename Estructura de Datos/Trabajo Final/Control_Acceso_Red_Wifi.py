# =============================================
# CONTROL DE ACCESOS A RED WIFI
# =============================================
# Desarrollado en Python
# Objetivo: Registrar dispositivos, validar límite de conexiones
# y generar alertas por accesos no autorizados
# =============================================

from tabulate import tabulate

# Lista principal para almacenar los dispositivos conectados
dispositivos = []

# Límite máximo de conexiones por usuario
LIMITE_CONEXIONES = 3

# -------------------------------------------------------------
# FUNCIONES DEL SISTEMA
# -------------------------------------------------------------

def RegistrarDispositivo():
    print("\n=== REGISTRO DE NUEVO DISPOSITIVO ===")
    usuario = input("Nombre del usuario: ").strip()
    mac = input("Dirección MAC (ej. AA:BB:CC:DD:EE:FF): ").strip().upper()
    ip = input("Dirección IP (ej. 192.168.1.10): ").strip()
    autorizado = input("¿Dispositivo autorizado? (s/n): ").lower()
    
    # Validar si ya existe la MAC
    for d in dispositivos:
        if d["MAC"] == mac:
            print("⚠️ Ya existe un dispositivo con esta MAC registrada.")
            return
    
    # Validar acceso (número de dispositivos por usuario)
    conexiones_usuario = sum(1 for d in dispositivos if d["Usuario"] == usuario)
    if conexiones_usuario >= LIMITE_CONEXIONES:
        print(f"🚫 El usuario '{usuario}' ha superado el límite de {LIMITE_CONEXIONES} conexiones simultáneas.")
        return
    
    # Registrar dispositivo
    nuevo = {
        "Usuario": usuario,
        "MAC": mac,
        "IP": ip,
        "Autorizado": "Sí" if autorizado == "s" else "No"
    }
    dispositivos.append(nuevo)
    print("✅ Dispositivo registrado exitosamente.")


def MostrarConexiones():
    print("\n=== DISPOSITIVOS CONECTADOS ===")
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    print(tabulate(dispositivos, headers="keys", tablefmt="grid"))


def ValidarAcceso():
    print("\n=== VALIDACIÓN DE ACCESO ===")
    mac = input("Ingrese la dirección MAC del dispositivo: ").strip().upper()
    encontrado = False
    for d in dispositivos:
        if d["MAC"] == mac:
            encontrado = True
            if d["Autorizado"] == "Sí":
                print(f"✅ Acceso permitido para {d['Usuario']} - IP: {d['IP']}")
            else:
                print(f"🚨 Acceso NO autorizado para {d['Usuario']} - MAC: {mac}")
            break
    if not encontrado:
        print("⚠️ Dispositivo no encontrado en el sistema.")


def GenerarAlertas():
    print("\n=== ALERTAS DE SEGURIDAD ===")
    alertas = []
    for d in dispositivos:
        if d["Autorizado"] == "No":
            alertas.append(f"🚨 Dispositivo NO autorizado detectado: {d['MAC']} ({d['Usuario']})")
    if not alertas:
        print("✅ No se detectaron accesos no autorizados.")
    else:
        for a in alertas:
            print(a)


def EliminarDispositivo():
    print("\n=== ELIMINAR DISPOSITIVO ===")
    mac = input("Ingrese la MAC del dispositivo a eliminar: ").strip().upper()
    for d in dispositivos:
        if d["MAC"] == mac:
            dispositivos.remove(d)
            print("🗑️ Dispositivo eliminado correctamente.")
            return
    print("⚠️ No se encontró un dispositivo con esa MAC.")


def MostrarContadores():
    total = len(dispositivos)
    autorizados = sum(1 for d in dispositivos if d["Autorizado"] == "Sí")
    no_autorizados = total - autorizados
    print("\n=== RESUMEN DE CONEXIONES ===")
    print(f"🔹 Total de dispositivos: {total}")
    print(f"✅ Autorizados: {autorizados}")
    print(f"🚨 No autorizados: {no_autorizados}")


# -------------------------------------------------------------
# MENÚ PRINCIPAL
# -------------------------------------------------------------
def menu():
    while True:
        print("\n===== CONTROL DE ACCESOS A RED WIFI =====")
        print("1. Registrar dispositivo")
        print("2. Mostrar conexiones")
        print("3. Validar acceso")
        print("4. Generar alertas")
        print("5. Eliminar dispositivo")
        print("6. Mostrar contadores")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            RegistrarDispositivo()
        elif opcion == "2":
            MostrarConexiones()
        elif opcion == "3":
            ValidarAcceso()
        elif opcion == "4":
            GenerarAlertas()
        elif opcion == "5":
            EliminarDispositivo()
        elif opcion == "6":
            MostrarContadores()
        elif opcion == "7":
            print("👋 Cerrando el sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# -------------------------------------------------------------
# INICIO DEL PROGRAMA
# -------------------------------------------------------------
menu()
