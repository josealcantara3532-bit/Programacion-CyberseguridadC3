import random

def loteria_simple(): #function to generate winning lottery number
    print("Bienvenido a la Lotería Simple") #welcome message
    #while True:
    print ("elige 3 numero entre 1 y 10") #prompt user to choose a number

#pedir al usuario que ingrese 3 números
    numeros_usuario = [] #list to store user numbers
    for i in range(3):
        while True:
            try:
                n = int(input(f"Ingrese el número {i+1}: ")) #input number
                if 1 <= n <= 10: #check if number is between 1 and 10
                    numeros_usuario.append(n) #add number to list
                    break
                else:
                    print("Por favor, ingrese un número entre 1 y 10.") #error message
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.") #error message

    #generar 3 números ganadores aleatorios entre 1 y 10
    numeros_ganadores = random.sample(range(1, 11), 3) #list comprehension to generate winning numbers
    print(" tus números son:", numeros_usuario) #print user numbers
    print("Números ganadores son:", numeros_ganadores) #print winning numbers

    #comparar números del usuario con los números ganadores
    aciertos = set(numeros_usuario) & set(numeros_ganadores)
    if aciertos:
        print(f"¡Felicidades! Has acertado los números: {len(aciertos)} numeros de aciertos {aciertos}") #print winning message
    else:
        print("Lo siento, no has acertado ningún número. ¡Inténtalo de nuevo!") #print losing message

    #quieres volver a jugar
    repertir = input("¿Quieres jugar de nuevo? (s/n): ").lower() #prompt user to play again
    if repertir != 's':
        print("\n gracias   por jugar hasta la proxima") #print new line
        return


#programa principal
loteria_simple() #call the lottery function1