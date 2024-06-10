"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,
además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que
había generado.

Author: Jesús Montañez Rodríguez
Fecha: 27-10-23
"""

import random

print("Programa para adivinar un número")

number_to_guess = random.randint(1, 100)
counter = 10


while True:
    number = int(input("Introduce un número: "))

    if number > number_to_guess:
        counter -= 1
        print(f"Introduce un número más pequeño, te quedan {counter} intentos")
        if counter == 0:
            break

    elif number < number_to_guess:
        counter -= 1
        print(f"Introduce un número más grande, te quedan {counter} intentos")
        if counter == 0:
            break
    else:
        print(f"Has Acertado el número es {number_to_guess}")
        break



