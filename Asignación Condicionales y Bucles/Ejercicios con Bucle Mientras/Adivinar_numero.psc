Algoritmo Adivinar_numero
	Definir numSecreto, intento Como Entero
	numSecreto <- 7
	
	Escribir "Adivina el número secreto (entre 1 y 10): "
	Leer intento
	
	Mientras intento <> numSecreto Hacer
		Escribir "Incorrecto, intenta otra vez: "
		Leer intento
	FinMientras
	
	Escribir "¡Correcto! El número secreto era ", numSecreto
	
FinAlgoritmo
