Algoritmo ContarPares
    Definir v, i, cont Como Entero
    Dimension v[10]
    cont <- 0
	
    Para i <- 1 Hasta 10 Hacer
        Escribir "Ingrese el número ", i, ": "
        Leer v[i]
        Si v[i] MOD 2 = 0 Entonces
            cont <- cont + 1
        FinSi
    FinPara
	
    Escribir "Cantidad de números pares: ", cont
FinAlgoritmo
