# EJERCICIO: ARTE ASCII CON BUCLES

# ==============================
# FUNCIÓN TRIÁNGULO
# ==============================
def triangulo(n):
    print("\n--- TRIÁNGULO ---")
    # Bucle de filas
    for i in range(1, n + 1):
        # Bucle de columnas
        for j in range(i):
            print("#", end=" ")
        print()


# ==============================
# FUNCIÓN CUADRADO
# ==============================
def cuadrado(n):
    print("\n--- CUADRADO ---")
    # Filas
    for i in range(n):
        # Columnas
        for j in range(n):
            print("#", end=" ")
        print()


# ==============================
# FUNCIÓN RECTÁNGULO (2:1)
# ==============================
def rectangulo(n):
    print(f"\n--- RECTÁNGULO ({n}x{n*2}) ---")
    # Filas
    for i in range(n):
        # Columnas (el doble)
        for j in range(n * 2):
            print("#", end=" ")
        print()


# ==============================
# FUNCIÓN CÍRCULO (APROXIMACIÓN)
# ==============================
def circulo(r):
    print(f"\n--- CÍRCULO (Radio {r}) ---")
    
    # Bucle eje Y
    for y in range(-r, r + 1):
        # Bucle eje X
        for x in range(-r, r + 1):
            
            # Fórmula del círculo: x² + y² <= r²
            if x*x + y*y <= r*r:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


# ==============================
# FUNCIÓN PENTÁGONO
# ==============================
def pentagono(n):
    print("\n--- PENTÁGONO ---")
    
    # Parte superior (triángulo)
    for i in range(1, n):
        print(" " * (n - i), end="")
        for j in range(2*i - 1):
            print("#", end="")
        print()
    
    # Parte inferior (rectángulo)
    for i in range(n):
        print("#" * (2*n - 1))


# ==============================
# MENÚ PRINCIPAL
# ==============================
while True:
    
    print("\n===== MENÚ DE FIGURAS =====")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Pentágono")
    print("6. Salir")
    
    opcion = input("Elige una opción: ")
    
    # Salida del programa
    if opcion == "6":
        print(" Programa finalizado")
        break
    
    # Pedir tamaño
    n = int(input("Ingrese el tamaño: "))
    
    # Llamar funciones según opción
    if opcion == "1":
        triangulo(n)
    elif opcion == "2":
        cuadrado(n)
    elif opcion == "3":
        rectangulo(n)
    elif opcion == "4":
        circulo(n)
    elif opcion == "5":
        pentagono(n)
    else:
        print(" Opción inválida")