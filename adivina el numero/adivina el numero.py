import random


def adivina_el_numero(x):

    print("=========================")
    print ("¡Bienvenido(a) al juego!")
    print("=========================")
    print ("Tu meta es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1, x) #número aleatorio entre 1 y x.

    predicción = 0

    while predicción != numero_aleatorio:
        #el usuario ingresa un numero
        predicción = int (input(f"Adivina un numero entre 1 y {x}: ")) #f-String permite reemplazar le valor de una expresion en nuestra codena

        if predicción < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif predicción > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")
        
    print(f"¡Felicitaciones! Adivinaste el número {numero_aleatorio} correctamente.")


adivina_el_numero(10)