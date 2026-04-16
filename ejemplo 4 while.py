# Ejemplo 4 while. Calcular la sumatoria de 8 pesos de articulos ingresados por el usuario

acum = 0
cont = 1

while cont <= 8:
    num = float(input("Digite el peso del artículo: "))
    acum += num
    cont += 1

print("El total es:", acum)
