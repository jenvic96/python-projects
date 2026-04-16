# Ejemplo 1 while. Sumar números hasta digitar 0

acum=0
num=None

while(num !=0) :
    num=int(input("Digite un número : "))
    acum=acum+num

print("El total es:",acum)
