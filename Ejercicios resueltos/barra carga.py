# EJERCICIO: SIMULADOR DE CARGA DE ARCHIVOS

import time  # Paso 1: Importar librería para manejar el tiempo

# ==============================
# ENTRADA DE DATOS
# ==============================

# Paso 2: Pedir tamaño del archivo
tamano = float(input("Ingrese el tamaño del archivo (MB): "))

# Paso 3: Pedir tiempo total de carga
tiempo_total = float(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {tamano} MB...\n")

# ==============================
# LÓGICA DE SIMULACIÓN
# ==============================

# Paso 4: Definir cantidad de pasos (ej: de 5% en 5% → 20 pasos)
pasos = 20

# Paso 5: Calcular tiempo por cada paso
tiempo_por_paso = tiempo_total / pasos

# ==============================
# BUCLE DE PROGRESO
# ==============================

for i in range(pasos + 1):
    
    # Paso 6: Calcular porcentaje actual
    porcentaje = int((i / pasos) * 100)
    
    # Paso 7: Construir barra de progreso
    llenos = "#" * i
    vacios = "-" * (pasos - i)
    
    barra = f"[{llenos}{vacios}]"
    
    # Paso 8: Mostrar barra en la misma línea
    print(f"\r{barra} {porcentaje}%", end="")
    
    # Paso 9: Esperar antes de actualizar
    time.sleep(tiempo_por_paso)

# ==============================
# MENSAJE FINAL
# ==============================

print(f"\n\n¡Archivo de {tamano} MB subido con éxito!")