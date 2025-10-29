# ---------------------------
# Mini-herramienta de Ciberseguridad (sin imports)
# ---------------------------

# 1) Escaneo simulado de hosts
def escanear_hosts_simulado(rango):
    """
    rango: cadena, puede ser:
      - "192.168.1.1" (un host)
      - "192.168.1.1-5" (último octeto de 1 a 5)
      - "192.168.1.1,192.168.1.10" (lista separada por comas)
    Retorna diccionario host -> estado (Activo/Inactivo)
    Regla simulada: si último octeto es par -> "Activo", impar -> "Inactivo"
    """
    hosts = []
    rango = rango.replace(" ", "")
    partes = rango.split(",")
    for p in partes:
        if "-" in p:
            base, rng = p.rsplit(".", 1)
            start_end = rng.split("-")
            if len(start_end) == 2 and start_end[0].isdigit() and start_end[1].isdigit():
                start = int(start_end[0])
                end = int(start_end[1])
                for i in range(start, end + 1):
                    hosts.append(base + "." + str(i))
            else:
                hosts.append(p)
        else:
            hosts.append(p)

    resultados = {}
    for h in hosts:
        try:
            ultimo = int(h.strip().split(".")[-1])
            estado = "Activo" if ultimo % 2 == 0 else "Inactivo"
        except:
            estado = "Formato inválido"
        resultados[h] = estado
    return resultados

# 2) Verificar seguridad de una contraseña (reglas simples)
def verificar_contraseña_simple(clave):
    """
    Devuelve diccionario con comprobaciones:
      - longitud
      - mayúsculas
      - minúsculas
      - dígitos
      - símbolos
      - contiene patrones comunes
      - puntuación final: 'Segura' / 'Débil'
    """
    minimo = 8
    tiene_may = False
    tiene_min = False
    tiene_num = False
    tiene_sym = False
    for ch in clave:
        if "A" <= ch <= "Z":
            tiene_may = True
        elif "a" <= ch <= "z":
            tiene_min = True
        elif "0" <= ch <= "9":
            tiene_num = True
        else:
            # consideramos cualquier otro como símbolo
            if ch.strip() != "":
                tiene_sym = True

    patrones = ["123", "password", "admin", "qwerty", "abcd"]
    contiene_patron = False
    for p in patrones:
        if p in clave.lower():
            contiene_patron = True
            break

    razones = []
    if len(clave) < minimo:
        razones.append(f"Menos de {minimo} caracteres")
    if not tiene_may:
        razones.append("Sin letras mayúsculas")
    if not tiene_min:
        razones.append("Sin letras minúsculas")
    if not tiene_num:
        razones.append("Sin números")
    if not tiene_sym:
        razones.append("Sin símbolos")
    if contiene_patron:
        razones.append("Contiene patrón común (123/password/admin/...)")

    puntuacion = "Segura" if len(razones) == 0 else "Débil"
    return {
        "contraseña": clave,
        "longitud": len(clave),
        "mayúsculas": tiene_may,
        "minúsculas": tiene_min,
        "dígitos": tiene_num,
        "símbolos": tiene_sym,
        "contiene_patrones_comunes": contiene_patron,
        "evaluación": puntuacion,
        "razones": razones
    }

# 3) Generador de combinaciones (limitado)
def generar_combinaciones(chars, longitud, limite=200):
    """
    Genera combinaciones de 'chars' con la 'longitud' indicada.
    Para evitar explosiones, se detiene después de 'limite' resultados impresos.
    Usa recursión controlada.
    """
    resultados = []
    contador = {"value": 0}  # mutable para cierre

    def rec(parcial):
        if contador["value"] >= limite:
            return
        if len(parcial) == longitud:
            resultados.append(parcial)
            contador["value"] += 1
            return
        for c in chars:
            if contador["value"] >= limite:
                break
            rec(parcial + c)

    # validaciones simples
    if longitud <= 0:
        return resultados
    if chars == "":
        return resultados

    rec("")
    return resultados

# 4) Contador de caracteres y palabras
def analizar_texto(texto):
    """
    Retorna número de caracteres, palabras, y longitud máxima de palabra.
    """
    caracteres = len(texto)
    palabras = texto.split()
    num_palabras = len(palabras)
    max_long = max((len(w) for w in palabras), default=0)
    return {
        "caracteres": caracteres,
        "palabras": num_palabras,
        "max_longitud_palabra": max_long
    }

# 5) Detección de patrones en texto (básico)
def detectar_patrones(texto):
    patrones = ["password", "pass", "admin", "1234", "qwerty", "token"]
    encontrados = []
    tx = texto.lower()
    for p in patrones:
        if p in tx:
            encontrados.append(p)
    return encontrados

# 6) Guardar resultados en archivo (append)
def guardar_resultados(archivo, texto):
    try:
        f = open(archivo, "a", encoding="utf-8")
        f.write(texto + "\n")
        f.close()
        return True
    except Exception as e:
        return False

# 7) Menú principal
def menu_ciberseguridad():
    while True:
        print("\n====== MINI-HERRAMIENTA CIBERSEGURIDAD ======")
        print("1) Escaneo simulado de hosts")
        print("2) Verificar seguridad de contraseña")
        print("3) Generar combinaciones (fuerza bruta educativa)")
        print("4) Analizar texto (caracteres / palabras)")
        print("5) Detectar patrones en texto")
        print("6) Guardar resultado en archivo")
        print("7) Salir")
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            entrada = input("Ingresa host(s) (ej: 192.168.1.2 o 192.168.1.1-5 o varios separados por comas): ")
            res = escanear_hosts_simulado(entrada)
            for h, e in res.items():
                print(f"{h} -> {e}")

        elif opcion == "2":
            clave = input("Ingresa la contraseña a evaluar: ")
            info = verificar_contraseña_simple(clave)
            print("Evaluación:", info["evaluación"])
            print("Longitud:", info["longitud"])
            if info["razones"]:
                print("Razones por las que es débil:")
                for r in info["razones"]:
                    print("-", r)
            else:
                print("No se detectaron problemas básicos.")

        elif opcion == "3":
            chars = input("Ingresa caracteres (ej: abc012): ")
            try:
                longitud = int(input("Longitud de las combinaciones (ej: 3): "))
            except:
                print("Longitud inválida.")
                continue
            try:
                limite = int(input("Límite de resultados a mostrar (por seguridad, ej: 100): "))
            except:
                limite = 200
            combos = generar_combinaciones(chars, longitud, limite)
            print(f"Se generaron {len(combos)} combinaciones (mostrando):")
            for c in combos:
                print(c)

        elif opcion == "4":
            texto = input("Ingresa texto a analizar: ")
            r = analizar_texto(texto)
            print("Caracteres:", r["caracteres"])
            print("Palabras:", r["palabras"])
            print("Máx longitud de palabra:", r["max_longitud_palabra"])

        elif opcion == "5":
            texto = input("Ingresa texto para buscar patrones: ")
            encontrados = detectar_patrones(texto)
            if encontrados:
                print("Patrones detectados:", ", ".join(encontrados))
            else:
                print("No se detectaron patrones comunes.")

        elif opcion == "6":
            archivo = input("Nombre de archivo (ej: resultados.txt): ")
            texto = input("Texto a guardar: ")
            ok = guardar_resultados(archivo, texto)
            if ok:
                print("Guardado correctamente en", archivo)
            else:
                print("Error al guardar.")

        elif opcion == "7":
            print("Saliendo... ¡hasta luego!")
            break

        else:
            print("Opción no válida. Intenta otra vez.")

# Ejecutar menú si el script se corre directamente
if __name__ == "__main__":
    menu_ciberseguridad()