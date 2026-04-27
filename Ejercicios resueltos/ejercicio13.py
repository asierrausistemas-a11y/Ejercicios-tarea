# EJERCICIO 13: TABLA DE MULTIPLICAR

# Paso 1: Pedir un número al usuario
numero = int(input("Ingrese un número: "))

# Paso 2: Usar un bucle for del 1 al 10
for i in range(1, 11):
    # Paso 3: Mostrar la multiplicación usando f-strings
    print(f"{numero} x {i} = {numero * i}")