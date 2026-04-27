# EJERCICIO 1: SALUDO PERSONALIZADO

def main():
    print("=== SALUDO PERSONALIZADO ===")

    # Pedir datos
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    # Año actual
    año_actual = 2026

    # Cálculo
    año_nacimiento = año_actual - edad

    # Resultado
    print("\nHola", nombre)
    print("Tienes", edad, "años")
    print("Naciste aproximadamente en", año_nacimiento)


if __name__ == "__main__":
    main()