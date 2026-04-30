# ============================================
# ESTADISTICAS DE EDADES - ESCUELA SAN PASCUALIN
# EMPRESA: DataByte
# ============================================

import datetime


# ============================================
# PARTE 1: IMPORTACION Y CONTROL DE ACCESO
# ============================================

# Esta funcion protege el sistema con una contrasena.
# El usuario tiene 3 intentos para escribirla bien.
def verificar_contrasena():
    CONTRASENA = "CursoPython"
    print("\nAcceso restringido - Ingrese la contrasena")
    intentos = 3

    while intentos > 0:
        clave = input("Contrasena: ")

        if clave == CONTRASENA:
            print("Acceso concedido. Bienvenido!\n")
            return True
        else:
            intentos -= 1
            print(f"Contrasena incorrecta. Intentos restantes: {intentos}")

    print("Acceso bloqueado por demasiados intentos fallidos.")
    return False


# ============================================
# PARTE 2: ENCABEZADO DEL SISTEMA
# ============================================

# Esta funcion muestra el titulo del proyecto, la empresa,
# la fecha actual y la hora actual.
def mostrar_fecha_hora():
    ahora = datetime.datetime.now()
    print("==============================================")
    print(" ESTADISTICAS - ESCUELA SAN PASCUALIN ")
    print(" Empresa: DataByte ")
    print("==============================================")
    print(f"Fecha: {ahora.strftime('%d/%m/%Y')}")
    print(f"Hora : {ahora.strftime('%I:%M:%S %p')}")
    print("==============================================")


# ============================================
# PARTE 3: INGRESO DE DATOS
# ============================================

# Esta funcion pide las edades de los alumnos.
# Solo acepta numeros enteros mayores que 0.
def ingresar_edades(n):
    edades = []
    print(f"\nIngresa las {n} edades de los alumnos:")

    for i in range(n):
        while True:
            try:
                edad = int(input(f"Alumno {i + 1}: "))
                if edad <= 0:
                    print("La edad debe ser mayor a 0.")
                else:
                    edades.append(edad)
                    break
            except ValueError:
                print("Ingresa un numero entero valido.")

    return edades


# ============================================
# PARTE 4: CALCULOS ESTADISTICOS
# ============================================

# Devuelve la edad mas alta dentro de la lista.
def edad_mayor(edades):
    return max(edades)


# Devuelve la edad mas baja dentro de la lista.
def edad_menor(edades):
    return min(edades)


# Calcula el promedio sumando todas las edades
# y dividiendo entre la cantidad de alumnos.
def calcular_promedio(edades):
    return sum(edades) / len(edades)


# La mediana es el valor central de los datos ordenados.
# Si hay cantidad impar, toma el del centro.
# Si hay cantidad par, saca el promedio de los dos del centro.
def calcular_mediana(edades):
    edades_ordenadas = sorted(edades)
    n = len(edades_ordenadas)
    medio = n // 2

    if n % 2 != 0:
        return edades_ordenadas[medio]
    else:
        return (edades_ordenadas[medio - 1] + edades_ordenadas[medio]) / 2


# ============================================
# PARTE 5: MENU Y PROGRAMA PRINCIPAL
# ============================================

# Esta funcion muestra las opciones del sistema.
def mostrar_menu():
    print("\n==============================================")
    print(" MENU ")
    print("==============================================")
    print("1. Ingresar edades de los alumnos")
    print("2. Mostrar edad mayor y menor")
    print("3. Calcular promedio de edades")
    print("4. Calcular mediana de edades")
    print("0. Salir")
    print("==============================================")


# Aqui empieza la ejecucion principal del programa.
# Primero se muestra el encabezado.
mostrar_fecha_hora()

# Solo se entra al sistema si la contrasena es correcta.
if verificar_contrasena():
    edades = []
    opcion = -1

    # El programa sigue repitiendo el menu hasta que el usuario
    # elija la opcion 0 para salir.
    while opcion != 0:
        mostrar_menu()

        try:
            opcion = int(input("Selecciona una opcion: "))
        except ValueError:
            print("Ingresa un numero valido.")
            continue

        if opcion == 1:
            try:
                n = int(input("\nCuantos alumnos tiene la muestra? "))
                if n <= 0:
                    print("El tamano debe ser mayor a 0.")
                else:
                    edades = ingresar_edades(n)
                    print(f"\nEdades registradas: {edades}")
            except ValueError:
                print("Ingresa un numero entero valido.")

        elif opcion == 2:
            if len(edades) == 0:
                print("\nPrimero debes ingresar las edades.")
            else:
                print(f"\nEdad mayor: {edad_mayor(edades)}")
                print(f"Edad menor: {edad_menor(edades)}")

        elif opcion == 3:
            if len(edades) == 0:
                print("\nPrimero debes ingresar las edades.")
            else:
                promedio = calcular_promedio(edades)
                print(f"\nPromedio de edades: {promedio:.1f}")

        elif opcion == 4:
            if len(edades) == 0:
                print("\nPrimero debes ingresar las edades.")
            else:
                mediana = calcular_mediana(edades)
                print(f"\nEdades ordenadas: {sorted(edades)}")
                print(f"Mediana: {mediana}")

        elif opcion == 0:
            print("\nHasta luego! - DataByte")

        else:
            print("\nOpcion no valida. Intenta de nuevo.")
