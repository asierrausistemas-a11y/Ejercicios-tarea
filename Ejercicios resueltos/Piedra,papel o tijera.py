"""""
1. Descripción de problema
Se solicita desarrolar un programa interactivo en Python que permita a un usuario
enfrentarse contra la computadora en el Clasico juego de Piedra, papel o tijera.
El programa debe ser capaz de procesar la entrada del usuario, generar una respuesta 
aleatoria y determinar un ganador basandose en las reglas tradicionales.

2. Requerimentos Técnicos
El algoritmo debe estrucuturarse de la siguiente manera:

*interfaz Visual: Mostrar un encabezado decorativo utilizando métodos de cadena como .center()
y multiplicacion de caracteres 

*Entrada de datos: Solicitar al usuario su eleccion. El programa debe ser capaz de reconocer
la entrada sin importar si se escribe en mayusculas o minusculas.

*inteligencia Aleatoria: La computadora debe elegir una opcion de una lista predefinida de
opciones (Piedra, Papel, Tijera)
de forma aleatoria utilizando el modulo random.

*Logica de comparación:
Implementar las conidiciones necesarias para evaluar.

1.Empate: Ambas elecciones son iguales.
2.Victoria: El usuario vence a la PC
(Piedra vence a Tijera, Tijera vence a Papel, Papel vence a Piedra)
3.Derrota: La PC vence al usuario

*Control de Flujo: El juego debe repetirse indefinidamente dentro de un bucle hasta que 
el usuario decida escribir la palabra (Salir)
"""

import random, time 

print("="*55)
print("Bienvenido al clasico juego de piedra, papel o tijera")
print("="*55)

opciones= ["piedra", "papel", "tijera"]


input("para empezar el juego(presiona enter)")


while True:
    usuario = input("escoja: piedra, papel o tijera (o salir):").lower()

    if usuario == "salir":
        print("Fin del juego")
        break

    pc = random.choice(opciones)

    print("Tú:", usuario)
    print("PC:", pc)

    if usuario == pc:
        print("Empate")
    elif usuario == "piedra" and pc == "tijera":
        print("Ganaste")
    elif usuario == "tijera" and pc == "papel":
        print("Ganaste")
    elif usuario == "papel" and pc == "piedra":
        print("Ganaste")
    else:
        print("Perdiste")






