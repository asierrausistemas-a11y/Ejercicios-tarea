# EJERCICIO 15: CONTADOR DE VOCALES

# Paso 1: Pedir una frase al usuario
frase = input("Ingrese una frase: ").lower()

# Paso 2: Crear un contador (empieza en 0)
contador = 0

# Paso 3: Recorrer cada letra de la frase
for letra in frase:
    
    # Paso 4: Verificar si la letra es una vocal
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        # Paso 5: Aumentar el contador
        contador += 1

# Paso 6: Mostrar el resultado
print("La cantidad de vocales es:", contador)