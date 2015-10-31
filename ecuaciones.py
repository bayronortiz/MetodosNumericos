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

plt.figure("Sistemas Ecuaciones")
plt.title("Sistemas de Ecuaciones")
f1, = plt.plot(v1, label="X2 = (-3/2) * X1 + 9")
f2, = plt.plot(v2, label="X2 = (X1/2) + 1")
plt.legend(handles=[f1,f2])
plt.grid(True)
plt.show()
