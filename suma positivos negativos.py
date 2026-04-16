# Suma de positivos y negativos

suma_positivos = 0
suma_negativos = 0

for i in range(15):
    num = int(input("Digite un número: "))

    if num > 0:
        suma_positivos += num
    else:
        suma_negativos += num

print("Suma de positivos:", suma_positivos)
print("Suma de negativos:", suma_negativos)
