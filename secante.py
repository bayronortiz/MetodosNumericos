# -*- coding:utf-8 -*-

'''
    Ejemplo de la funcion: f(x)= e^(-x) - x
    Método Númerico Secante

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
Ea = 0
Et = 0
x_ant = 0  # Xi-1    anterior
xi = 1    # Xi actual
x_sig = 0    # Xi+1     siguiente

print "Epsilon = ", ES ,"\n"
print "{0:3s} | {1:15s} | {2:15s} | {3:15s}".format("i", "Xi", "Ea", "Et")

while True:
    x_sig = xi - ((funcion(xi) * (xi - x_ant)) / (funcion(xi) - funcion(x_ant))) # Calcula termino siguiente

    if i != 0:
        Ea = abs((xi - x_ant) / xi) * 100    # Error Aproximado
        Et = abs ((VVR - xi) / VVR ) * 100    # Error Verdadero

    print "{0:3d} | {1:15f} | {2:15e} | {3:15e}".format(i, xi, Ea, Et)

    if abs(Ea) < ES and i != 0:
        break

    x_ant = xi
    xi = x_sig
    i += 1