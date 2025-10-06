Algoritmo Suma_10_numeros
	Definir num, suma, i Como Real
	suma <- 0
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		Escribir "Ingrese el número ", i, ": "
		Leer num
		suma <- suma + num
	FinPara
	
	Escribir "La suma total es: ", suma
	
FinAlgoritmo
