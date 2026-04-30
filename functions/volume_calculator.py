#Este programa: Permite al usuario seleccionar
#una figura (cubo, esfera o cilindro), solicita los datos necesarios,
#calcula el volumen utilizando funciones y muestra el resultado con 2 decimales.


import math

# -------- FUNCIONES --------

def volumen_cubo(lado):
    return lado ** 3

def volumen_esfera(radio):
    return (4/3) * math.pi * (radio ** 3)

def volumen_cilindro(radio, altura):
    return math.pi * (radio ** 2) * altura


# -------- PROGRAMA PRINCIPAL --------

opcion = 0  # variable de control

while opcion != 4:  # se repite hasta que el usuario elija salir

    print("\n--- MENÚ DE VOLÚMENES ---")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Cilindro")
    print("4. Salir")

    opcion = int(input("Digite una opción: "))

    if opcion == 1:
        lado = float(input("Digite el lado del cubo: "))
        resultado = volumen_cubo(lado)
        print("Volumen del cubo:", round(resultado, 2))

    elif opcion == 2:
        radio = float(input("Digite el radio de la esfera: "))
        resultado = volumen_esfera(radio)
        print("Volumen de la esfera:", round(resultado, 2))

    elif opcion == 3:
        radio = float(input("Digite el radio del cilindro: "))
        altura = float(input("Digite la altura del cilindro: "))
        resultado = volumen_cilindro(radio, altura)
        print("Volumen del cilindro:", round(resultado, 2))

    elif opcion == 4:
        print("Fin del programa")

    else:
        print("Opción inválida")
