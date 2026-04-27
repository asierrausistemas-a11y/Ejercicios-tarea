# EJERCICIO 20: SUCESIÓN DE FIBONACCI

# Paso 1: Pedir cantidad de términos
n = int(input("¿Cuántos términos desea ver?: "))

# Paso 2: Definir los dos primeros valores
a = 0
b = 1

# Paso 3: Mostrar la serie usando un bucle for
for i in range(n):
    # Paso 4: Mostrar el número actual
    print(a, end=" ")
    
    # Paso 5: Calcular el siguiente número
    siguiente = a + b
    
    # Paso 6: Actualizar valores
    a = b
    b = siguiente