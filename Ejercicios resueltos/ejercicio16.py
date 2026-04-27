# EJERCICIO 16: ADIVINA EL NÚMERO (CON INTENTOS)

# Paso 1: Definir el número secreto
numero_secreto = 7  # (puedes cambiarlo si quieres)

# Paso 2: Definir la cantidad de intentos
intentos = 5

# Paso 3: Bucle con límite de intentos
for i in range(intentos):
    
    # Paso 4: Pedir número al usuario
    numero = int(input("Adivina el número (1-20): "))
    
    # Paso 5: Comparar con el número secreto
    if numero == numero_secreto:
        print("🎉 ¡Correcto! Adivinaste el número")
        break  # Paso 6: Terminar el bucle si acierta
    
    elif numero < numero_secreto:
        print("El número es MAYOR")
    
    else:
        print("El número es MENOR")

# Paso 7: Mensaje si no adivinó en los intentos
else:
    print("😢 Se acabaron los intentos. El número era:", numero_secreto)