# -*-coding: utf-8 -*-

# Resuelve por método númerico de punto fijo e^-x  -  x

import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt
import math

l_xi = []    #Lista de los xi

xi = 0
i = 0
Ea = 0
x_ant = 0

n_iter = input("Ingrese N° Iteraciones--> ")    # N° de Iteraciones

print "{0:2s} | {1:10s} | {2:10s}".format("i","Xi","Ea%")

while i <= n_iter:
    x_ant = xi
    xi = math.exp(-xi)  #Calcula el valor de c/u de las iteraciones
    Ea = abs((xi - x_ant) / xi) * 100

    print "{0:2d} | {1:10.8f} | {2:10.8f}".format(i, xi, Ea)

    i += 1