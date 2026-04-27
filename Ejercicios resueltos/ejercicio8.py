# EJERCICIO 8: AÑO BISIESTO

# Paso 1: Pedir el año al usuario
año = int(input("Ingrese un año: "))

# Paso 2: Evaluar si es bisiesto
# Regla:
# - Debe ser divisible por 4
# - NO debe ser divisible por 100, EXCEPTO si es divisible por 400

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    # Paso 3: Mostrar si es bisiesto
    print("El año es BISIESTO")
else:
    # Paso 4: Mostrar si no es bisiesto
    print("El año NO es bisiesto")