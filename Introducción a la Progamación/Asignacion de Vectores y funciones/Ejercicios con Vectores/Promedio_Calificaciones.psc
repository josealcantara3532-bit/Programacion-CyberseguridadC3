Algoritmo PromedioCalificaciones
    Definir notas, i Como Entero
    Definir suma, promedio Como Real
    Dimension notas[5]
    suma <- 0
	
    Para i <- 1 Hasta 5 Hacer
        Escribir "Ingrese la nota del estudiante ", i, ": "
        Leer notas[i]
        suma <- suma + notas[i]
    FinPara
	
    promedio <- suma / 5
    Escribir "El promedio del grupo es: ", promedio
FinAlgoritmo
