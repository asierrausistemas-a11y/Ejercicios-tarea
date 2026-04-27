# EJERCICIO 19: CAJA REGISTRADORA

# Paso 1: Crear variable acumuladora
total = 0

# Paso 2: Bucle para ingresar precios
while True:
    # Paso 3: Pedir precio
    precio = float(input("Ingrese el precio del producto (0 para terminar): "))
    
    # Paso 4: Verificar si el usuario quiere terminar
    if precio == 0:
        break  # Salir del bucle
    
    # Paso 5: Sumar el precio al total
    total += precio

# Paso 6: Aplicar descuento si supera 100
if total > 100:
    descuento = total * 0.10
else:
    descuento = 0

# Paso 7: Calcular total final
total_pagar = total - descuento

# Paso 8: Mostrar resultados
print("\n=== RESULTADO ===")
print("Total de la compra:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)