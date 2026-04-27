# EJERCICIO 9: CALCULADORA DE IMC

# Paso 1: Pedir el peso en kg
peso = float(input("Ingrese su peso (kg): "))

# Paso 2: Pedir la altura en metros
altura = float(input("Ingrese su altura (m): "))

# Paso 3: Calcular el IMC
# Fórmula: IMC = peso / (altura^2)
imc = peso / (altura ** 2)

# Paso 4: Clasificar el IMC

# Bajo peso
if imc < 18.5:
    categoria = "Bajo peso"

# Normal
elif imc >= 18.5 and imc <= 24.9:
    categoria = "Normal"

# Sobrepeso
elif imc >= 25 and imc <= 29.9:
    categoria = "Sobrepeso"

# Obesidad
else:
    categoria = "Obesidad"

# Paso 5: Mostrar resultados
print("\n=== RESULTADO ===")
print("IMC:", round(imc, 2))
print("Categoría:", categoria)