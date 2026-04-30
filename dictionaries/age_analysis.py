# Programa para almacenar edades de 15 personas

personas = {}

# 🔹 CARGA DE DATOS
print("Ingrese los datos de 15 personas")

for i in range(15):
    nombre = input(f"Ingrese el nombre {i+1}: ").capitalize()
    edad = int(input("Ingrese la edad: "))
    personas[nombre] = edad

opcion = 0

# 🔹 MENÚ
while opcion != 7:

    print("\n--- MENÚ ---")
    print("1. Mostrar edad mayor")
    print("2. Cuántos menores de edad")
    print("3. Cuántos adultos mayores")
    print("4. Mostrar nombres")
    print("5. Mostrar rango de edades")
    print("6. Ordenar nombres alfabéticamente")
    print("7. Salir")

    opcion = int(input("Digite una opción: "))

    # 🔹 1. EDAD MAYOR
    if opcion == 1:
        mayor = max(personas.values())
        print("La edad mayor es:", mayor)

    # 🔹 2. MENORES DE EDAD (<18)
    elif opcion == 2:
        cont = 0
        for edad in personas.values():
            if edad < 18:
                cont += 1
        print("Cantidad de menores de edad:", cont)

    # 🔹 3. ADULTOS MAYORES (>=65)
    elif opcion == 3:
        cont = 0
        for edad in personas.values():
            if edad >= 65:
                cont += 1
        print("Cantidad de adultos mayores:", cont)

    # 🔹 4. MOSTRAR NOMBRES
    elif opcion == 4:
        print("Lista de nombres:")
        for nombre in personas.keys():
            print(nombre)

    # 🔹 5. RANGO (mayor - menor)
    elif opcion == 5:
        mayor = max(personas.values())
        menor = min(personas.values())
        rango = mayor - menor
        print("El rango de edades es:", rango)

    # 🔹 6. ORDENAR NOMBRES
    elif opcion == 6:
        nombres_ordenados = sorted(personas.keys())
        print("Nombres ordenados:")
        for nombre in nombres_ordenados:
            print(nombre)

    elif opcion == 7:
        print("Fin del programa")

    else:
        print("Opción incorrecta")
