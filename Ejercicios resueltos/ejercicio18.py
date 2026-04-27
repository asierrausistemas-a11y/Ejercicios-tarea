# EJERCICIO 18: CAJERO AUTOMÁTICO BÁSICO

# Paso 1: Definir saldo inicial
saldo = 1000

# Paso 2: Crear bucle infinito para el menú
while True:
    # Paso 3: Mostrar opciones
    print("\n=== CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    # Paso 4: Pedir opción al usuario
    opcion = input("Seleccione una opción: ")

    # Paso 5: Evaluar opción 1
    if opcion == "1":
        print("Su saldo es:", saldo)

    # Paso 6: Evaluar opción 2
    elif opcion == "2":
        retiro = float(input("Ingrese el monto a retirar: "))
        
        # Verificar si hay suficiente saldo
        if retiro <= saldo:
            saldo -= retiro  # Restar dinero
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("Fondos insuficientes")

    # Paso 7: Evaluar opción 3
    elif opcion == "3":
        print("Gracias por usar el cajero")
        break  # Salir del bucle

    # Paso 8: Opción inválida
    else:
        print("Opción no válida, intente de nuevo")