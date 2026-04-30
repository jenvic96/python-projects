# Promedio de 10 edades

acum = 0
cont = 1

while cont <= 10:
    edad = int(input("Digite una edad: "))
    acum += edad
    cont += 1

promedio = acum / 10

print("El promedio es:", promedio)
