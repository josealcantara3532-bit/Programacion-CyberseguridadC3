Algoritmo Validar_contraseña
	Definir contraseña Como Cadena
	
	Escribir "Ingrese la contraseña: "
	Leer contrasena
	
	Mientras contraseña <> "1234" Hacer
		Escribir "Contraseña incorrecta. Intente de nuevo: "
		Leer contraseña
	FinMientras
	
	Escribir "¡Acceso autorizado!"
FinAlgoritmo
