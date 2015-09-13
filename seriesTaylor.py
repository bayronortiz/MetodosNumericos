# -*- coding: utf-8 -*-

# Fecha: 08-Sept-2015

from math import *


# Calcula la serie Taylor de la funcion fx=Cos (x)
# Param xi:Xi -- xii: Xi+1
def fxN(xi,xii,n):
    h= xii-xi
    valor= 0    # Guarda el valor de la funcion
    temp= 0    # Guarda el valor temporal de la funcion
    negativo= False
    signo=(1,-1,-1, 1)
    cs= 0  #Controlador de signo

    for i in range(n+1):
        if i%2==0:
            temp= (signo[cs]*cos(xi) * h**i)/factorial(i)
        else:
            temp= (signo[cs]*sin(xi) * h**i)/factorial(i)

        cs+=1
        if cs == 4:       #Reiniciamos controlador de signo
            cs= 0

        valor+= temp    #Sumamos a valor serie taylor

    return valor

n= input("Ingrese el Orden (n)--> ")

print "Orden  |  f(xi+1)"

#Falta hallar el error aproximado
for i in range(n+1):
    print "%d  |  %.9f" % (i, fxN(pi/4,pi/3,i))



