import os

print("Directorio actual:", os.getcwd())

nuevo_directorio = "nueva_carpeta"
os.makedirs(nuevo_directorio, exist_ok=True)
print(f"Directorio '{nuevo_directorio}' creado.")
