import ipaddress
from tabulate import tabulate

# Lista principal (inventario)
inventario = []

# -------------------------------
# Función para validar direcciones IP
# -------------------------------
def validar_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# -------------------------------
# Registrar nuevo equipo
# -------------------------------
def registrar_equipo():
    print("\n--- REGISTRO DE EQUIPO ---")
    nombre = input("Nombre del equipo: ").strip()
    tipo = input("Tipo de equipo (Router, Switch, Access Point, etc.): ").strip()
    ubicacion = input("Ubicación del equipo: ").strip()
    ip = input("Dirección IP: ").strip()

    # Validar IP
    if not validar_ip(ip):
        print("❌ IP inválida. Registro cancelado.")
        return

    # Evitar duplicados por IP
    for equipo in inventario:
        if equipo["ip"] == ip:
            print("❌ Ya existe un equipo con esa IP. Registro cancelado.")
            return
    
    estado = input("Estado (activo/inactivo): ").lower().strip()
    if estado not in ["activo", "inactivo"]:
        print("❌ Estado no válido.")
        return

    # Crear diccionario del equipo
    equipo = {
        "nombre": nombre,
        "tipo": tipo,
        "ubicacion": ubicacion,
        "ip": ip,
        "estado": estado
    }

    inventario.append(equipo)
    print("✅ Equipo registrado exitosamente.")

# -------------------------------
# Mostrar inventario completo
# -------------------------------
def mostrar_inventario():
    print("\n--- INVENTARIO DE EQUIPOS ---")
    if not inventario:
        print("No hay equipos registrados.")
        return

    # Crear tabla para mostrar
    tabla = []
    for eq in inventario:
        fila = [eq["nombre"], eq["tipo"], eq["ubicacion"], eq["ip"], eq["estado"]]
        tabla.append(fila)

    encabezados = ["Nombre", "Tipo", "Ubicación", "IP", "Estado"]
    print(tabulate(tabla, headers=encabezados, tablefmt="grid"))

# -------------------------------
# Generar alertas de equipos inactivos
# -------------------------------
def generar_alertas():
    print("\n--- ALERTAS DE EQUIPOS ---")
    alertas = []
    for eq in inventario:
        if eq["estado"] == "inactivo":
            alertas.append(f"{eq['nombre']} ({eq['ip']}) está INACTIVO en {eq['ubicacion']}")

    if alertas:
        for alerta in alertas:
            print("⚠️", alerta)
    else:
        print("✅ Todos los equipos están activos.")

# -------------------------------
# Editar equipo
# -------------------------------
def editar_equipo():
    print("\n--- EDITAR EQUIPO ---")
    if not inventario:
        print("No hay equipos registrados.")
        return

    ip_buscar = input("Ingrese la IP del equipo que desea editar: ").strip()
    for eq in inventario:
        if eq["ip"] == ip_buscar:
            print(f"Equipo encontrado: {eq['nombre']} ({eq['tipo']}) en {eq['ubicacion']}")
            nuevo_nombre = input(f"Nuevo nombre (actual: {eq['nombre']}): ").strip()
            nuevo_tipo = input(f"Nuevo tipo (actual: {eq['tipo']}): ").strip()
            nueva_ubicacion = input(f"Nueva ubicación (actual: {eq['ubicacion']}): ").strip()
            nuevo_estado = input(f"Nuevo estado (activo/inactivo) (actual: {eq['estado']}): ").lower().strip()

            # Solo cambia si se ingresa algo nuevo
            if nuevo_nombre: eq["nombre"] = nuevo_nombre
            if nuevo_tipo: eq["tipo"] = nuevo_tipo
            if nueva_ubicacion: eq["ubicacion"] = nueva_ubicacion
            if nuevo_estado in ["activo", "inactivo"]: eq["estado"] = nuevo_estado

            print("✅ Equipo actualizado correctamente.")
            return

    print("❌ No se encontró un equipo con esa IP.")

# -------------------------------
# Eliminar equipo
# -------------------------------
def eliminar_equipo():
    print("\n--- ELIMINAR EQUIPO ---")
    if not inventario:
        print("No hay equipos registrados.")
        return

    ip_buscar = input("Ingrese la IP del equipo a eliminar: ").strip()
    for eq in inventario:
        if eq["ip"] == ip_buscar:
            print(f"Equipo encontrado: {eq['nombre']} ({eq['tipo']}) en {eq['ubicacion']}")
            confirmar = input("¿Seguro que desea eliminarlo? (s/n): ").lower().strip()
            if confirmar == "s":
                inventario.remove(eq)
                print("🗑️ Equipo eliminado correctamente.")
            else:
                print("❌ Eliminación cancelada.")
            return

    print("❌ No se encontró un equipo con esa IP.")

# -------------------------------
# Contadores de equipos
# -------------------------------
def mostrar_contadores():
    print("\n--- RESUMEN DE EQUIPOS ---")
    total = len(inventario)
    activos = sum(1 for eq in inventario if eq["estado"] == "activo")
    inactivos = sum(1 for eq in inventario if eq["estado"] == "inactivo")

    print(f"🔹 Total de equipos registrados: {total}")
    print(f"✅ Equipos activos: {activos}")
    print(f"⚠️ Equipos inactivos: {inactivos}")

# -------------------------------
# Menú principal
# -------------------------------
def menu():
    while True:
        print("\n===== SISTEMA DE INVENTARIO DE EQUIPOS DE RED =====")
        print("1. Registrar equipo")
        print("2. Mostrar inventario")
        print("3. Generar alertas")
        print("4. Editar equipo")
        print("5. Eliminar equipo")
        print("6. Mostrar contadores")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_equipo()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            generar_alertas()
        elif opcion == "4":
            editar_equipo()
        elif opcion == "5":
            eliminar_equipo()
        elif opcion == "6":
            mostrar_contadores()
        elif opcion == "7":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

# -------------------------------
# Inicio del programa
# -------------------------------
menu()
