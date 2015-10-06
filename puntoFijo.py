# -*-coding: utf-8 -*-

# Resuelve por método númerico de punto fijo e^-x  -  x

import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt
import math

ES = 0.5*10**(2-6)
#l_xi = []    #Lista de los xi

VVR = 0.56714329    # Constante Valor Verdadero de la Raíz
i = 0
Ea = 0    # Error Aproximado
Et = 0    # Error Verdadero
xi = 0    # Xi actual
x_sig = 0    #Xi+1    siguiente
x_ant = 0     # xi-1 anterior

#n_iter = input("Ingrese N° Iteraciones--> ")    # N° de Iteraciones


print "{0:2s} | {1:10s} | {2:10s} | {3:10s}".format("i","Xi","Ea%", "Et%")

while True:
    x_sig= math.exp(-xi)  #Calcula el valor de c/u de las iteraciones

    if i != 0:
        Ea = abs((xi - x_ant) / xi) * 100

    Et = abs((VVR - xi) / VVR) * 100

    print "{0:2d} | {1:10.8f} | {2:10.8f} | {3:10.8f} ".format(i, xi, Ea, Et)

    if abs(Ea) < ES and i != 0:
        break

    x_ant = xi
    xi = x_sig
    i += 1