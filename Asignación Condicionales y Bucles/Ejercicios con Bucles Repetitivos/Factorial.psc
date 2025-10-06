Algoritmo Factorial
	Definir num, i, fact Como Entero
	
	Escribir "Ingrese un número (entero no negativo): "
	Leer num
	
	Si num < 0 Entonces
		Escribir "Error: el factorial no está definido para números negativos."
	Sino
		fact <- 1
		Para i <- 1 Hasta num Con Paso 1 Hacer
			fact <- fact * i
		FinPara
		Escribir "El factorial de ", num, " es: ", fact
	FinSi
	
FinAlgoritmo
