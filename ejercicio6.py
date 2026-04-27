# EJERCICIO 6: CATEGORÍA DE EDAD

# Paso 1: Pedir la edad al usuario
edad = int(input("Ingrese su edad: "))

# Paso 2: Evaluar cada rango de edad

# Si está entre 0 y 12
if edad >= 0 and edad <= 12:
    print("Eres un Niño")

# Si está entre 13 y 17
elif edad >= 13 and edad <= 17:
    print("Eres un Adolescente")

# Si está entre 18 y 64
elif edad >= 18 and edad <= 64:
    print("Eres un Adulto")

# Si es 65 o más
elif edad >= 65:
    print("Eres un Adulto mayor")

# Paso 3: Validación por si ingresan algo inválido
else:
    print("Edad no válida")