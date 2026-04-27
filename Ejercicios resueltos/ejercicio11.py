# EJERCICIO 11: CUENTA REGRESIVA

# Paso 1: Pedir un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Paso 2: Usar un bucle while para la cuenta regresiva
while numero >= 0:
    # Paso 3: Mostrar el número actual
    print(numero)
    
    # Paso 4: Disminuir el número en 1 (decremento)
    numero -= 1

# Paso 5: Mensaje final
print("¡Despegue!")