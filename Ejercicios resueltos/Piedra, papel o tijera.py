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
