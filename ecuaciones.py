# -*- coding:utf-8 -*-

'''
	Graficar funciones.

    Elaborado Bayron Danilo Ortiz Foronda
'''


from math import *
from matplotlib import pyplot as plt


#Funcion X2=-(3/2)X1+9
def funcion1(x):
	return -(3.0/2.0)*x + 9


#Funcion X2= (X1/2) + 1
def funcion2(x):
	return (x/2.0) + 1


v1 = []
v2 = []

for i in range(10):
	v1.append(funcion1(i))
	v2.append(funcion2(i))

plt.plot(v1)
plt.plot(v2)
plt.grid(True)

plt.show()



