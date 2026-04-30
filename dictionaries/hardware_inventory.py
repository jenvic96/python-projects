# Sistema de inventario de ferretería

# Diccionario inicial: articulo -> cantidad
inventario = {
    "martillo": 10,
    "clavos": 50,
    "destornillador": 15
}

opcion = 0

while opcion != 6:

    print("\n--- MENÚ FERRETERÍA ---")
    print("1. Agregar artículo")
    print("2. Modificar artículo")
    print("3. Consultar artículo")
    print("4. Eliminar artículo")
    print("5. Mostrar tuplas del diccionario")
    print("6. Salir")

    opcion = int(input("Digite una opción: "))

    # 🔹 1. AGREGAR ARTÍCULO
    if opcion == 1:
        art = input("Ingrese el nombre del artículo: ").lower()

        if art in inventario:
            print("El artículo ya existe")
        else:
            cant = int(input("Ingrese la cantidad: "))
            inventario[art] = cant
            print("Artículo agregado correctamente")

    # 🔹 2. MODIFICAR ARTÍCULO
    elif opcion == 2:
        art = input("Ingrese el artículo a modificar: ").lower()

        if art in inventario:
            cant = int(input("Ingrese la nueva cantidad: "))
            inventario[art] = cant
            print("Artículo modificado correctamente")
        else:
            print("El artículo no existe")

    # 🔹 3. CONSULTAR ARTÍCULO
    elif opcion == 3:
        art = input("Ingrese el artículo a consultar: ").lower()

        if art in inventario:
            print("Cantidad disponible:", inventario[art])
        else:
            print("El artículo no existe")

    # 🔹 4. ELIMINAR ARTÍCULO
    elif opcion == 4:
        art = input("Ingrese el artículo a eliminar: ").lower()

        if art in inventario:
            del inventario[art]
            print("Artículo eliminado correctamente")
        else:
            print("El artículo no existe")

    # 🔹 5. MOSTRAR TUPLAS
    elif opcion == 5:
        print("Tuplas del diccionario:")

        # items() convierte el diccionario en tuplas
        for elemento in inventario.items():
            print(elemento)

    # 🔹 6. SALIR
    elif opcion == 6:
        print("Fin del programa")

    else:
        print("Opción incorrecta")
