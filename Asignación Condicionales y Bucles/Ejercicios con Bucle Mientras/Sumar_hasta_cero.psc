Algoritmo Sumar_hasta_cero
	Definir num, suma Como Real
	suma <- 0
	
	Escribir "Ingrese un número (0 para terminar): "
	Leer num
	
	Mientras num <> 0 Hacer
		suma <- suma + num
		Escribir "Ingrese otro número (0 para terminar): "
		Leer num
	FinMientras
	
	Escribir "La suma total es: ", suma
	
FinAlgoritmo
