#!/usr/bin/env python3
# tool_ciberseguridad.py
# Versión con librerías estándar — uso educativo y responsable

import os # para operaciones del sistema
import subprocess # para ejecutar comandos del sistema
import socket # para operaciones de red
import itertools # para generación de combinaciones
import re # para expresiones regulares
from pathlib import Path # para manejo de rutas
from datetime import datetime # para timestamps

# ---------------------------
# Utilidades de red y archivos
# ---------------------------

LOG_DIR = Path("logs") # directorio de logs
LOG_DIR.mkdir(exist_ok=True) # crear si no existe
LOG_FILE = LOG_DIR / f"ciber_tool_{datetime.now().strftime('%Y%m%d')}.log" # archivo de log diario

def log(text): #function to log messages
    """Registra texto con timestamp en archivo de logs.""" # docstring
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # timestamp
    line = f"[{ts}] {text}" # línea a escribir
    try: # escribir en archivo
        with LOG_FILE.open("a", encoding="utf-8") as f: # append mode
            f.write(line + "\n") # escribir línea
    except Exception as e: # manejar errores
        print("Error al escribir log:", e)  #imprimir error
    # también imprimimos
    print(line) # imprimir en consola

# ---------------------------
# 1) Escaneo real: ping y check de puertos
# ---------------------------

def hacer_ping(ip, timeout=1): #function to ping
    """
    Realiza un ping al host. Devuelve True si responde, False en otro caso.
    Funciona en Windows y Unix (usa -n o -c según plataforma).
    """
    param = "-n" if os.name == "nt" else "-c" # parámetro según OS
    cmd = ["ping", param, "1", "-W", str(timeout), ip] if os.name != "nt" else ["ping", param, "1", ip] # comando ping
    try: #| ejecutar comando
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) # ejecutar sin mostrar salida
        ok = (res.returncode == 0)  # verificar código de retorno
        log(f"ping {ip} -> {'activo' if ok else 'inactivo'}")  # registrar resultado
        return ok       # devolver resultado
    except Exception as e:  # manejar errores
        log(f"ping {ip} -> error ({e})")    # registrar error
        return False    # devolver falso en error

def puerto_abierto(host, puerto, timeout=1.0):   #function to check open port   
    """
    Comprueba si un puerto TCP está abierto en host.
    Devuelve True/False.
    """     # crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # establecer timeout
    s.settimeout(timeout)
    try:    
        res = s.connect_ex((host, puerto))  # intentar conectar
        s.close()      # cerrar socket 
        abierto = (res == 0)            # verificar resultado1 
        log(f"check puerto {host}:{puerto} -> {'abierto' if abierto else 'cerrado'}")
        return abierto
    except Exception as e:
        log(f"check puerto {host}:{puerto} -> error ({e})")
        return False

def escanear_puertos_rango(host, inicio=1, fin=1024, timeout=0.5, max_puertos=200):
    """
    Escanea puertos TCP en el rango [inicio, fin]. Por seguridad limita la cantidad de puertos escaneados.
    Retorna lista de puertos abiertos.
    """
    abiertos = []
    total = min(fin - inicio + 1, max_puertos)
    count = 0
    for puerto in range(inicio, fin + 1):
        if count >= total:
            break
        if puerto_abierto(host, puerto, timeout):
            abiertos.append(puerto)
        count += 1
    return abiertos

# ---------------------------
# 2) Verificador de contraseñas
# ---------------------------

COMMON_PATTERNS = [r"123", r"password", r"admin", r"qwerty", r"abcd", r"pass", r"letmein"]

def verificar_contraseña(clave):
    """
    Evaluación simple de contraseña: longitud, clases de caracteres y patrones comunes.
    Devuelve diccionario con resultados.
    """
    reglas = {
        "longitud": len(clave),
        "mayusculas": bool(re.search(r"[A-Z]", clave)),
        "minusculas": bool(re.search(r"[a-z]", clave)),
        "digitos": bool(re.search(r"\d", clave)),
        "simbolos": bool(re.search(r"[^A-Za-z0-9]", clave)),
        "contiene_patron": False,
        "patrones_encontrados": []
    }
    lows = clave.lower()
    for p in COMMON_PATTERNS:
        if p in lows:
            reglas["contiene_patron"] = True
            reglas["patrones_encontrados"].append(p)

    razones = []
    if reglas["longitud"] < 8:
        razones.append("menos de 8 caracteres")
    if not reglas["mayusculas"]:
        razones.append("sin mayúsculas")
    if not reglas["minusculas"]:
        razones.append("sin minúsculas")
    if not reglas["digitos"]:
        razones.append("sin dígitos")
    if not reglas["simbolos"]:
        razones.append("sin símbolos")
    if reglas["contiene_patron"]:
        razones.append("contiene patrón común: " + ", ".join(reglas["patrones_encontrados"]))

    reglas["evaluacion"] = "Segura" if not razones else "Débil"
    reglas["razones"] = razones
    log(f"verificar_contraseña -> evaluación: {reglas['evaluacion']} ({', '.join(razones) if razones else 'sin problemas básicos'})")
    return reglas

# ---------------------------
# 3) Generador de combinaciones (itertools)
# ---------------------------

def generar_combinaciones_iter(chars, longitud, limite=200):
    """
    Genera combinaciones usando itertools.product.
    Devuelve una lista (hasta 'limite' resultados).
    """
    if longitud <= 0 or not chars:
        return []
    productos = itertools.product(chars, repeat=longitud)
    resultados = []
    for i, prod in enumerate(productos):
        if i >= limite:
            break
        resultados.append("".join(prod))
    log(f"generar_combinaciones_iter -> generado {len(resultados)} combos (chars='{chars}', len={longitud})")
    return resultados

# ---------------------------
# 4) Analizar texto y detectar patrones
# ---------------------------

DEFAULT_PATTERNS = [r"password", r"pass", r"admin", r"\d{4,}", r"token", r"api[_-]?key"]

def analizar_texto(texto):
    palabras = texto.split()
    resultado = {
        "caracteres": len(texto),
        "palabras": len(palabras),
        "max_longitud_palabra": max((len(w) for w in palabras), default=0)
    }
    log(f"analizar_texto -> caracteres={resultado['caracteres']}, palabras={resultado['palabras']}")
    return resultado

def detectar_patrones_regex(texto, patrones=None):
    if patrones is None:
        patrones = DEFAULT_PATTERNS
    encontrados = []
    tx = texto.lower()
    for p in patrones:
        try:
            if re.search(p, tx):
                encontrados.append(p)
        except re.error:
            # patrón inválido, saltar
            continue
    log(f"detectar_patrones_regex -> encontrados: {encontrados if encontrados else 'ninguno'}")
    return encontrados

# ---------------------------
# 5) Guardado seguro de resultados
# ---------------------------

def guardar_resultado(nombre_archivo, texto):
    ruta = Path(nombre_archivo)
    try:
        with ruta.open("a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat()}] {texto}\n")
        log(f"guardar_resultado -> guardado en {ruta}")
        return True
    except Exception as e:
        log(f"guardar_resultado -> error: {e}")
        return False

# ---------------------------
# Menú principal interactivo
# ---------------------------

def menu():
    while True:
        print("\n====== HERRAMIENTA CIBERSEGURIDAD (con librerías) ======")
        print("1) Ping a host")
        print("2) Escanear puertos (rango limitado)")
        print("3) Verificar contraseña")
        print("4) Generar combinaciones (itertools)")
        print("5) Analizar texto")
        print("6) Detectar patrones (regex)")
        print("7) Guardar texto en archivo")
        print("8) Salir")
        op = input("Elige (1-8): ").strip()

        if op == "1":
            ip = input("Host o IP: ").strip()
            ok = hacer_ping(ip)
            print(f"{ip} -> {'Activo' if ok else 'Inactivo'}")

        elif op == "2":
            host = input("Host/IP a escanear: ").strip()
            try:
                ini = int(input("Puerto inicio (ej: 1): ").strip())
                fin = int(input("Puerto fin (ej: 1024): ").strip())
            except:
                print("Rango inválido.")
                continue
            abiertos = escanear_puertos_rango(host, ini, fin, timeout=0.4, max_puertos=500)
            if abiertos:
                print("Puertos abiertos:", ", ".join(str(p) for p in abiertos))
            else:
                print("No se encontraron puertos abiertos en el rango escaneado (o no respondió).")

        elif op == "3":
            clave = input("Contraseña a evaluar: ")
            res = verificar_contraseña(clave)
            print("Evaluación:", res["evaluacion"])
            if res["razones"]:
                print("Razones:")
                for r in res["razones"]:
                    print("-", r)
            else:
                print("No se detectaron problemas básicos.")

        elif op == "4":
            chars = input("Carácteres (ej: abc012): ").strip()
            try:
                longitud = int(input("Longitud combinaciones: ").strip())
                limite = int(input("Límite de resultados a mostrar (ej: 100): ").strip())
            except:
                print("Valores inválidos.")
                continue
            combos = generar_combinaciones_iter(chars, longitud, limite)
            print(f"Generadas: {len(combos)} (mostrando):")
            for c in combos:
                print(c)

        elif op == "5":
            texto = input("Texto a analizar: ")
            r = analizar_texto(texto)
            print("Caracteres:", r["caracteres"])
            print("Palabras:", r["palabras"])
            print("Máx longitud palabra:", r["max_longitud_palabra"])

        elif op == "6":
            texto = input("Texto para búsqueda con regex: ")
            patrones = input("Patrones separados por comas (opcional, enter para default): ").strip()
            pats = [p.strip() for p in patrones.split(",")] if patrones else None
            encontrados = detectar_patrones_regex(texto, pats)
            if encontrados:
                print("Patrones detectados:", ", ".join(encontrados))
            else:
                print("No se detectaron patrones comunes.")

        elif op == "7":
            archivo = input("Nombre archivo donde guardar (ej: resultados.txt): ").strip()
            texto = input("Texto a guardar: ").strip()
            if guardar_resultado(archivo, texto):
                print("Guardado correctamente.")
            else:
                print("Error al guardar.")

        elif op == "8":
            print("Saliendo. ¡Usa con responsabilidad!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú al ejecutar el script
if __name__ == "__main__":
    menu()