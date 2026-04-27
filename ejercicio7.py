# EJERCICIO 7: DESCUENTO EN LA TIENDA

# Paso 1: Pedir el total de la compra
total = float(input("Ingrese el total de la compra: "))

# Paso 2: Evaluar el descuento según el monto

# Si es menor a 50 → no hay descuento
if total < 50:
    descuento = 0

# Si está entre 50 y 100 → 5% de descuento
elif total >= 50 and total <= 100:
    descuento = total * 0.05

# Si es mayor a 100 → 10% de descuento
else:
    descuento = total * 0.10

# Paso 3: Calcular el total a pagar
total_pagar = total - descuento

# Paso 4: Mostrar resultados
print("\n=== RESULTADO ===")
print("Total original:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)