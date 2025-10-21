Algoritmo SumaVector
    Definir v, i, suma Como Entero
    Dimension v[10]
    suma <- 0
	
    Para i <- 1 Hasta 10 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer v[i]
        suma <- suma + v[i]
    FinPara
	
    Escribir "La suma total es: ", suma
FinAlgoritmo
