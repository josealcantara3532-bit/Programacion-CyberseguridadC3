#!/usr/bin/env python3
import subprocess
import sys
import xml.etree.ElementTree as ET

def instalar_dependencias():
    try:
        import nmap
    except ImportError:
        print("Instalando python-nmap...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-nmap"])
        print("¡Instalación completada!")

def escanear_vulnerabilidades(objetivo):
    try:
        import nmap
    except ImportError:
        print("Error: No se pudo importar nmap. Instala las dependencias primero.")
        return

    scanner = nmap.PortScanner()
    
    print(f"\nIniciando escaneo de vulnerabilidades en {objetivo}")
    print("Este escaneo es solo con fines educativos!")
    
    try:
        # Escaneo con detección de vulnerabilidades
        resultado = scanner.scan(
            hosts=objetivo,
            arguments='-sV --script vuln -p 21,22,23,80,443,445,3389'
        )
        
        # Mostrar resultados
        print("\n" + "="*50)
        print("RESULTADOS DEL ESCANEO")
        print("="*50)
        
        for host in scanner.all_hosts():
            print(f"\nHost: {host}")
            print(f"Estado: {scanner[host].state()}")
            
            for proto in scanner[host].all_protocols():
                print(f"\nProtocolo: {proto}")
                puertos = scanner[host][proto].keys()
                
                for port in puertos:
                    print(f"\nPuerto {port}/{proto}")
                    estado = scanner[host][proto][port]['state']
                    print(f"Estado: {estado}")
                    
                    if 'name' in scanner[host][proto][port]:
                        servicio = scanner[host][proto][port]['name']
                        print(f"Servicio: {servicio}")
                    
                    if 'product' in scanner[host][proto][port]:
                        producto = scanner[host][proto][port]['product']
                        print(f"Producto: {producto}")
                    
                    if 'version' in scanner[host][proto][port]:
                        version = scanner[host][proto][port]['version']
                        print(f"Versión: {version}")
                    
                    # Mostrar información de vulnerabilidades
                    if 'script' in scanner[host][proto][port]:
                        for script in scanner[host][proto][port]['script']:
                            print(f"\n[VULNERABILIDAD] {script}")
                            print(f"Detalles: {scanner[host][proto][port]['script'][script]}")
    
    except Exception as e:
        print(f"Error durante el escaneo: {str(e)}")

def main():
    print("Escáner de Vulnerabilidades Educativo")
    print("=" * 40)
    print("ADVERTENCIA: Este software es solo para fines educativos.")
    print("No escanees sistemas sin permiso explícito.\n")
    
    objetivo = input("Ingresa el objetivo (ej. 192.168.1.1 o scanme.nmap.org): ").strip()
    
    if not objetivo:
        print("Error: Debes especificar un objetivo")
        sys.exit(1)
    
    instalar_dependencias()
    escanear_vulnerabilidades(objetivo)

if __name__ == "__main__":
    main()