Algoritmo Tabla_Multiplicar
	Definir num, i, resultado Como Entero
	
	Escribir "Ingrese un número para ver su tabla de multiplicar: "
	Leer num
	
	Para i <- 1 Hasta 10 Con Paso 1 Hacer
		resultado <- num * i
		Escribir num, " x ", i, " = ", resultado
	FinPara
FinAlgoritmo
