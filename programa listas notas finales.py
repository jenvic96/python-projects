# Programa para trabajar con 15 notas finales de Cálculo 1
#El programa usa una lista para guardar las notas y un menú para que el usuario
#pueda calcular el promedio, encontrar la nota mayor o menor, ver el rango y eliminar datos.


# Aquí guardamos las 15 notas en una lista (como una lista en papel)
notas = [85, 90, 78, 88, 92, 67, 74, 81, 95, 89, 76, 84, 91, 73, 80]

# Esta variable sirve para saber qué opción eligió el usuario
opcion = 0

# Este ciclo repite el menú hasta que el usuario elija salir (opción 6)
while opcion != 6:

    print("\n--- MENÚ DE NOTAS ---")
    print("1. Nota mayor")
    print("2. Promedio")
    print("3. Rango")
    print("4. Eliminar nota")
    print("5. Nota menor")
    print("6. Salir")

    # El usuario escribe un número
    opcion = int(input("Digite una opción: "))

    # 1. NOTA MAYOR
    if opcion == 1:
        # max busca el número más grande de la lista
        print("La nota mayor es:", max(notas))

    # 2. PROMEDIO
    elif opcion == 2:
        # sum suma todo
        # len cuenta cuántos números hay
        promedio = sum(notas) / len(notas)

        # round(...,1) deja solo 1 decimal
        print("El promedio es:", round(promedio, 1))

    # 3. RANGO
    elif opcion == 3:
        # rango = mayor - menor
        rango = max(notas) - min(notas)
        print("El rango es:", rango)

    # 4. ELIMINAR NOTA
    elif opcion == 4:
        eliminar = int(input("Digite la nota que desea eliminar: "))

        # preguntamos si la nota está en la lista
        if eliminar in notas:
            # remove borra ese número
            notas.remove(eliminar)
            print("Nota eliminada")
            print("Lista nueva:", notas)
        else:
            print("Esa nota no existe")

    # 5. NOTA MENOR
    elif opcion == 5:
        # min busca el número más pequeño
        print("La nota menor es:", min(notas))

    # 6. SALIR
    elif opcion == 6:
        print("Fin del programa")

    # Si el usuario escribe algo incorrecto
    else:
        print("Opción incorrecta")
