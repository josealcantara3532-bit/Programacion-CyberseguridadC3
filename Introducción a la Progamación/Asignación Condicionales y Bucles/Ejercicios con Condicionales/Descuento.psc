Algoritmo Descuento
	Definir monto, total Como Real
	Escribir "Introduzca el monto de la compra"
	Leer monto
	Si monto > 500 Entonces
		total <- monto * 0.9
		Escribir "Se aplico un 10% de descuento. Totak a pagar: ", total
	SiNo
		Escribir "No aplica descuento. Total a pagar: ", monto
	Fin Si
FinAlgoritmo
