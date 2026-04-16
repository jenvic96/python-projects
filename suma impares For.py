# Ejemplo programa que solicite 10 numeros y calcule la suma de los impares


acum=0

for num in range(10):
    valor=int(input("Digite un numero entero: "))
    if(valor % 2 == 1):
        acum+=valor

print("La suma de impares es : ", acum)
              
print (" \n Fin de Programa !")
