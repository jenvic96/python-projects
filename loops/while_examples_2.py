# Ejemplo 2 while. Escriba el algoritmo de un programa que calcule el producto de 7 numeros decimales

acum=1
num=None
cont=1

while(cont<=7) :
    num=float(input("Digite un número : "))
    acum*=num  #acum=acum*num
    cont+=1  #cont=cont+1

print("El total es:",acum)
