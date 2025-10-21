Funcion prom <- Promedio(n1, n2, n3)
    prom <- (n1 + n2 + n3) / 3
FinFuncion

Algoritmo PromedioNotas
    Definir a, b, c, prom Como Real
    Escribir "Ingrese tres notas: "
    Leer a, b, c
    prom <- Promedio(a, b, c)
    Escribir "El promedio es: ", prom
    Si prom >= 70 Entonces
        Escribir "Aprobado."
    Sino
        Escribir "Reprobado."
    FinSi
FinAlgoritmo
