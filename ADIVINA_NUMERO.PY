'''Codigo básico para crear un juego que se llamae : Adivina el Numero" el cual se basa en usar la librería
random para adivinar un numero aleatorio en un rango de numeros del 1 al 100 y se cuenta con 8 oportunidades
parte de formaciones realizadas en mi proceso de aprendizaje de programación usando el lenguaje Python'''

from random import *

Nombre=input("Por favor ingrese su nombre: ")
print(f"Bueno {Nombre} he pensado un numero al azar entre 1 y 100\n quieres adivinarlo? \ntienes 8 intentos")
valor= randint(1,100)
intentos=0

while intentos < 8:
    numero = int(input("Ingresa un numero del 1 al 100: "))
    intentos = intentos + 1
    if numero < 1 or numero > 100:
        print("Su numero esta fuera del rango exigido")
    elif numero < valor:
        print("Su numero es mas bajo que el correcto")
    elif numero > valor:
        print("Su numero es mayor que el correcto")
    else:
        print(f"Felicidades has acertado el numero en el intento {intentos}")
        break
if numero != valor:
    print(f"Lo siento has agotado tus intentos, el numero secreto era {valor}")



