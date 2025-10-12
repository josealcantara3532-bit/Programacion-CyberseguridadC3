Funcion valida <- ValidarPassword(pass)
    Si Longitud(pass) > 8 Entonces
        valida <- Verdadero
    Sino
        valida <- Falso
    FinSi
FinFuncion

Algoritmo PasswordSegura
    Definir clave Como Cadena
    Escribir "Ingrese una contraseña: "
    Leer clave
    Si ValidarPassword(clave) Entonces
        Escribir "Contraseña válida."
    Sino
        Escribir "Contraseña NO válida (debe tener más de 8 caracteres)."
    FinSi
FinAlgoritmo
