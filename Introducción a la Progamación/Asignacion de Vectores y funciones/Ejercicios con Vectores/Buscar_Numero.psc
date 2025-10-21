Algoritmo BuscarNumero
    Definir v, i, buscado Como Entero
    Definir encontrado Como Logico
    Dimension v[8]
    encontrado <- Falso
	
    Para i <- 1 Hasta 8 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer v[i]
    FinPara
	
    Escribir "Ingrese el número a buscar: "
    Leer buscado
	
    Para i <- 1 Hasta 8 Hacer
        Si v[i] = buscado Entonces
            encontrado <- Verdadero
        FinSi
    FinPara
	
    Si encontrado Entonces
        Escribir "El número se encuentra en el vector."
    Sino
        Escribir "El número NO se encuentra en el vector."
    FinSi
FinAlgoritmo
