# Crear la lista
puertos_abiertos = [22, 80, 443, 8080]

# a) Agregar el puerto 21
puertos_abiertos.append(21)
print("a) Lista después de agregar 21:", puertos_abiertos)

# b) Eliminar el puerto 8080
puertos_abiertos.remove(8080)
print("b) Lista después de eliminar 8080:", puertos_abiertos)

# c) Mostrar la lista ordenada
puertos_abiertos.sort()
print("c) Lista ordenada:", puertos_abiertos)

print("\n")