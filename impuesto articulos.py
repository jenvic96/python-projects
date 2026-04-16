# Calcular impuesto y precio final de 12 artículos

for i in range(12):
    precio = float(input("Digite el precio del artículo: "))

    impuesto = precio * 0.13
    total = precio + impuesto

    print("Impuesto (13%):", impuesto)
    print("Precio con impuesto:", total)
    print("------------------------")
