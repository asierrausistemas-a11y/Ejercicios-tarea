# EJERCICIO 12: SUMA DE LOS PRIMEROS N NÚMEROS

# Paso 1: Pedir el número N
N = int(input("Ingrese un número: "))

# Paso 2: Crear una variable acumuladora (empieza en 0)
suma = 0

# Paso 3: Usar un bucle for desde 1 hasta N
for i in range(1, N + 1):
    # Paso 4: Ir sumando cada número
    suma += i

# Paso 5: Mostrar el resultado final
print("La suma de los primeros", N, "números es:", suma)