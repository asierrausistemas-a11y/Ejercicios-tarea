# EJERCICIO 10: APROBACIÓN DE CRÉDITO

# Paso 1: Pedir el salario mensual
salario = float(input("Ingrese su salario mensual: "))

# Paso 2: Preguntar si tiene deudas (convertimos a minúscula)
deuda = input("¿Tiene deudas? (si/no): ").lower()

# Paso 3: Evaluar las condiciones para aprobar el crédito
# Condiciones:
# - Salario mayor a 1000
# - NO tener deudas

if salario > 1000 and deuda == "no":
    # Paso 4: Mostrar si cumple ambas condiciones
    print("Crédito Aprobado")
else:
    # Paso 5: Mostrar si no cumple
    print("Crédito Denegado")