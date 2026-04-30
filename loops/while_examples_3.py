# Ejemplo 3 while. Escriba el algoritmo que sume numeros hasta digitar 0

acum=0
num=None


while True:
    num=float(input("Digite un número : "))
    acum+=num  #acum=acum*num
    if num==0:
        break
    
print("El total es:",acum)
