#Pide 5 notas, calcula la suma y el promedio final
suma_notas = 0
for _ in range(5):
    nota = float(input("Ingrese una nota: "))
    suma_notas += nota
promedio = suma_notas / 5
print(f"La suma de las notas es: {suma_notas}")
print(f"El promedio final es: {promedio}")
