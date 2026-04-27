# EJERCICIO 2: PAR O IMPAR

# Paso 1: Pedir al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Paso 2: Usar el operador módulo (%) para saber si es divisible entre 2
# Si el residuo es 0, el número es par
if numero % 2 == 0:
    # Paso 3: Mostrar resultado si es par
    print("El número es PAR")
else:
    # Paso 4: Mostrar resultado si es impar
    print("El número es IMPAR")