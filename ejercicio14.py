# EJERCICIO 14: ADIVINA EL PIN

# Paso 1: Definir el PIN secreto
pin_secreto = "1234"

# Paso 2: Pedir el PIN al usuario por primera vez
pin = input("Ingrese el PIN: ")

# Paso 3: Usar un bucle while hasta que el PIN sea correcto
while pin != pin_secreto:
    # Paso 4: Mensaje de error
    print("PIN incorrecto, intenta de nuevo")
    
    # Paso 5: Volver a pedir el PIN
    pin = input("Ingrese el PIN: ")

# Paso 6: Si sale del while, el PIN es correcto
print("PIN correcto, acceso concedido")