Algoritmo InventarioEquipos
    Definir equipos, ubicaciones, IPsEquipos, estadoEquipo Como Cadena
    Dimension equipos[100]
    Dimension ubicaciones[100]
    Dimension IPsEquipos[100]
    Dimension estadoEquipo[100]
	
    Definir totalEquipos, opcion, i Como Entero
    Definir nombre, ip, tipo, ubi Como Cadena
	
    totalEquipos <- 0
	
    Repetir
        Escribir ""
        Escribir "=== Inventario de Equipos ==="
        Escribir "1. Registrar equipo"
        Escribir "2. Mostrar inventario"
        Escribir "3. Generar alertas (no disponibles)"
        Escribir "4. Cambiar estado de equipo"
        Escribir "5. Salir"
        Leer opcion
		
        Segun opcion Hacer
            1:
                Escribir "Nombre equipo:"; Leer nombre
                Escribir "IP:"; Leer ip
                Escribir "Tipo:"; Leer tipo
                Escribir "Ubicación:"; Leer ubi
                totalEquipos <- totalEquipos + 1
                equipos[totalEquipos] <- nombre
                IPsEquipos[totalEquipos] <- ip
                ubicaciones[totalEquipos] <- ubi
                estadoEquipo[totalEquipos] <- "Disponible"
                Escribir "Equipo registrado. ID = ", totalEquipos
            2:
                Si totalEquipos = 0 Entonces
                    Escribir "No hay equipos registrados."
                Sino
                    Escribir "----- Inventario -----"
                    Para i <- 1 Hasta totalEquipos Hacer
                        Escribir i, ". ", equipos[i], " | IP:", IPsEquipos[i], " | Ubic:", ubicaciones[i], " | Estado:", estadoEquipo[i]
                    FinPara
                FinSi
            3:
                Escribir "----- Alertas: equipos no disponibles -----"
                Para i <- 1 Hasta totalEquipos Hacer
                    Si estadoEquipo[i] <> "Disponible" Entonces
                        Escribir "Alerta: ", equipos[i], " - Estado: ", estadoEquipo[i]
                    FinSi
                FinPara
            4:
                Si totalEquipos = 0 Entonces
                    Escribir "No hay equipos para cambiar."
                Sino
                    Escribir "Seleccione ID de equipo (1-", totalEquipos, "):"; Leer i
                    Si i < 1 O i > totalEquipos Entonces
                        Escribir "ID inválido."
                    Sino
                        Escribir "Estado actual: ", estadoEquipo[i]
                        Escribir "Ingrese nuevo estado (Disponible/Ocupado/Fuera de servicio):"; Leer estadoEquipo[i]
                        Escribir "Estado actualizado."
                    FinSi
                FinSi
            5:
                Escribir "Saliendo..."
            De Otro Modo:
                Escribir "Opcion invalida."
        FinSegun
    Hasta Que opcion = 5
FinAlgoritmo
