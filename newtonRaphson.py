# -*- coding:utf-8 -*-

'''
    Ejemplo de la funcion: f(x)= e^(-x) - x
    Método Númerico NewtonRaphson

    Elaborado Bayron Danilo Ortiz Foronda
'''

import math

# Calcula el valor en x de la fucion e^-x -x
def funcion(x):
    return math.exp(-x) - x

# Calcula el valor en x de la funcion derivada
def derivada(x):
    return -math.exp(-x) - 1


ES = 0.5*10**(2-6)    # Constante Cifras significativas
VVR = 0.56714329    # Constante Valor Verdadero de la Raíz
i = 0    #Iteraciones
xi = 0    # Xi actual
Ea = 0
Et = 0
x_sig = 0    # Xi+1     siguiente
x_ant = 0  # Xi-1    anterior

print "Epsilon = ", ES ,"\n"
print "{0:3s} | {1:15s} | {2:15s} | {3:15s}".format("i", "Xi", "Ea", "Et")

while True:
    x_sig = xi - (funcion(xi) / derivada(xi)) # Calcula termino siguiente

    if xi != 0:
        Ea = abs((xi - x_ant) / xi) * 100    # Error Aproximado

    Et = abs ((VVR - xi) / VVR ) * 100    # Error Verdadero

    print "{0:3d} | {1:10f} | {2:10e} | {3:10e}".format(i, xi, Ea, Et)

    if abs(Ea) < ES and i != 0:
        break

    x_ant = xi
    xi = x_sig
    i += 1