#ejemplo funcion

import math # Biblioteca matematica

def hipotenusa(cat1,cat2):
     h=math.sqrt(math.pow(cat1,2)+math.pow(cat2,2))
     return h

c1=float(input("Digite cateto 1 :"))
c2=float(input("Digite cateto 2 :"))

print("La medida de la hipotenusa es :", hipotenusa(c1,c2))
