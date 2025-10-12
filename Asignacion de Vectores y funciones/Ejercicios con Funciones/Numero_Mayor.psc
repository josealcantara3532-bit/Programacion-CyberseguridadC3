Funcion mayor <- MayorNumero(a, b, c)
    mayor <- a
    Si b > mayor Entonces
        mayor <- b
    FinSi
    Si c > mayor Entonces
        mayor <- c
    FinSi
FinFuncion

Algoritmo NumeroMayor
    Definir a, b, c, maximo Como Entero
    Escribir "Ingrese tres números: "
    Leer a, b, c
    maximo <- MayorNumero(a, b, c)
    Escribir "El número mayor es: ", maximo
FinAlgoritmo
