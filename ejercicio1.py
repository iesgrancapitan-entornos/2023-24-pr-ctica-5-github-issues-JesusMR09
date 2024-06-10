"""
Programa para adivinar un número

Author: Jesús Montañez Rodríguez
Fecha: 27/10/23
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
