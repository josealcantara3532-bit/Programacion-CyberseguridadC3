# Crear la tupla
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

# a) Mostrar el segundo elemento
print("a) Segundo elemento:", vulnerabilidades[1])

# b) Mostrar los dos últimos elementos
print("b) Dos últimos elementos:", vulnerabilidades[-2:])

# c) Intentar modificar un elemento (provocará error)
print("c) Intentando modificar un elemento (esto generará un error):")
try:
    vulnerabilidades[0] = "Modificación"
except TypeError as e:
    print("Error:", e)

print("\n")
