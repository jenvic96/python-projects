#Este programa solicita los lados de un triángulo, calcula su área
#utilizando la fórmula de Herón mediante una función y muestra el resultado.


import math  # Importamos la librería para usar sqrt (raíz cuadrada)

# Creamos la función
def area_triangulo(a, b, c):
    # Paso 1: calcular el semiperímetro (s)
    s = (a + b + c) / 2  
    
    # Paso 2: aplicar fórmula de Herón
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Paso 3: devolver el resultado
    return area


# ---------------- PROGRAMA PRINCIPAL ----------------

# Pedimos los datos al usuario
lado1 = float(input("Digite el lado 1: "))
lado2 = float(input("Digite el lado 2: "))
lado3 = float(input("Digite el lado 3: "))

# Llamamos la función (mandamos los valores)
resultado = area_triangulo(lado1, lado2, lado3)

# Mostramos el resultado
print("El área del triángulo es:", round(resultado, 2))
