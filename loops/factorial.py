# Programa para calcular el factorial de un número

# n es una variable que guarda el número que ingresa el usuario
# input() permite escribir datos desde el teclado
# int() convierte ese dato a número entero
n = int(input("Digite un número: "))

# Variable donde se va a guardar el resultado del factorial
# Empieza en 1 porque vamos a multiplicar
factorial = 1

# Ciclo for que repite el proceso
# range(n, 0, -1) significa:
# empezar en n (el número ingresado por el usuario)
# terminar en 1
# ir disminuyendo de 1 en 1
for i in range(n, 0, -1):

    # Multiplicamos el valor actual por i
    # Esto acumula el resultado del factorial
    factorial *= i

# Mostrar el resultado final
print("El factorial de", n, "es:", factorial)
