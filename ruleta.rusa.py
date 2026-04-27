"""
Reto de programación simulador de probabilidades: ruleta rusa

1. Descripción del problema:
se requiere desarollar un programa en python que simule un sistema de azar basado 
en un revolver de 6 recamaras. El programa debe gestionar eventos aleatorios, pausas
de ejecucion para mejorar la experiencia del usuario y control de flujo basado en 
condiciones de victoria o derrota.

2. Requerimentos técnicos:

el algoritmo debe cumplir con los siguientes requisitos:

*inicialización: Definir una recamara ganadora (bala) de forma aleatoria entre 1 y 6. (random)

*Bucle de juego: El usuario debe interactuar manualmente para girar el tambor y disparar (time)
(While)

*Mecánica de azar: En cada turno, la posición de la recamara que queda al frente el al percutor
debe ser aleatoria, simulando el giro del tambor.

*condición de derrota: si la recamara seleccionada coincide con la de la bala, el programa
termina automáticamente.  (if)

*condición de victoria: El jugador  gana si logra sobrevivir a 5 intentos (ya que el sexto
intento sería el fatal).  (else)
"""
import random, time 

print("="*50)
print("Bienvenido al Simulador de la ruleta rusa")
print("="*50)

input("poner bala en el tambor (Presiona Enter)")
bala = random.randint(1,6)
time.sleep(0.5)

disparos = 0 #variable para contar los disparos realizados

while True:
    input("Girar el tambor (presionar enter)")
    recamara = random.randint(1,6)

    input("apuntar y disparar (presiona enter)")
    time.sleep(1)

    if recamara == bala:
        print("!Bang¡ Has perdido. La bala estaba en la recamara " /
        "numero", bala)
        break
    else:
        disparos += 1
        print("Has sobrevivido a este intento")
        print("intentos de Disparos", disparos)

    if disparos == 5:
        print("¡Felicitaciones! has ganado al sobrevivir a 5 intentos.")
        break

print("="*50)
print("Fin del juego - Gracias por jugar")
print("="*50)





