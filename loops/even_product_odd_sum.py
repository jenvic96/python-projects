# Producto de pares y suma de impares

producto_pares = 1
suma_impares = 0
cont = 1

while cont <= 12:
    num = int(input("Digite un número: "))

    if num % 2 == 0:
        producto_pares *= num
    else:
        suma_impares += num

    cont += 1

print("Producto de pares:", producto_pares)
print("Suma de impares:", suma_impares)
