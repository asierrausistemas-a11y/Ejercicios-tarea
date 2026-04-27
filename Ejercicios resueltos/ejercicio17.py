# EJERCICIO 17: VALIDADOR DE NÚMEROS PRIMOS

# Paso 1: Pedir un número al usuario
numero = int(input("Ingrese un número: "))

# Paso 2: Asumimos que el número ES primo (bandera)
es_primo = True

# Paso 3: Validar que sea mayor a 1
if numero <= 1:
    es_primo = False
else:
    # Paso 4: Probar divisiones desde 2 hasta numero-1
    for i in range(2, numero):
        
        # Paso 5: Si es divisible por algún número → NO es primo
        if numero % i == 0:
            es_primo = False
            break  # Paso 6: Salir del bucle

# Paso 7: Mostrar resultado
if es_primo:
    print("El número es PRIMO")
else:
    print("El número NO es primo")