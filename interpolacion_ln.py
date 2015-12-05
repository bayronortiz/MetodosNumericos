#-*-coding: utf-8 -*-

'''
    Descripción: Script interpolación lineal de la función logaritmo natural e
                 interpolación cuadrática.

    Elaborado:    Bayron Danilo Ortiz Foronda.

    Version Python: 2.7
'''

import math
import matplotlib.pyplot as plt
import numpy as np

#Funcion lambda global logaritmo natural
f = lambda x: math.log(x)

# Funcion que calcula la pendiente de la funcion
def m(x0, x1):
    fx0 = f(x0)
    fx1 = f(x1)

    return (fx1 - fx0) / (x1 - x0)

#Funcion que calcula la interpolación dentro de un rango
def interpol(x0, x1, x):
    fx0 = f(x0)
    fx1 = f(x1)

    fx = fx0 + m(x0,x1) * (x - x0)

    return fx

#Inicio del Programa
x = range(1,7)        # Creamos el vector de 1 a 6
fx = []
v_interpol = []
v_ep = np.arange(1,6,0.1)
fep = []        #funcion epsilon, guarda los valores ln continuo (funcion original)

for xi in x:
    fx.append(f(xi))
    v_interpol.append(interpol(xi, xi+1, xi))

for i in v_ep:
    fep.append(f(i))

# Graficamos modelo dispersion y la recta de regresión modelo2
plt.figure(u"Gráfica Interpolación Lineal")
plt.title(u"Interpolación Ln x", fontweight="bold")
plt.plot(x,fx, "ro", label= "Ln(x) Discreto")        #Valores dispersion
plt.plot(x,v_interpol, label=u"Interpolación Lineal", lw=1.5)          #Interpolacion lineal
plt.plot(v_ep,fep, label=u"Ln(x) Original", lw=1.5)
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()