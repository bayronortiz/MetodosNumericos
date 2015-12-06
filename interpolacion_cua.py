#-*-coding: utf-8 -*-

'''
    Descripción: Script interpolación cuadrática de la función logaritmo natural.

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

#Funcion que calcula la interpolacion cuadratica
def interpol_cua(x0, x1, x2, x):
    fx0 = f(x0)
    fx1 = f(x1)
    fx2 = f(x2)

    b0 = f(x0)
    b1 = m(x0,x1)

    b2 = (m(x1,x2) - m(x0,x1)) / (x2 - x0)

    return b0 + b1 * (x - x0) + b2 * (x - x0) * (x - x1)

#Inicio del Programa
x = range(1,7)        # Creamos el vector de 1 a 6
fx = []
v_interpol_cua = []
v_ep = np.arange(1,6,0.1)    # valores para fep, con incremento epsilon 0.1
fep = []    #Logaritmo natural continuo. funcion epsilon

for xi in x:
    fx.append(f(xi))
    v_interpol_cua.append(interpol_cua(xi, xi+1, xi+2, xi))

for i in v_ep:
    fep.append(f(i))

# Graficamos modelo dispersion y la recta de regresión modelo2
plt.figure(u"Gráfica Interpolación Cuadrática")
plt.title(u"Interpolación Cuadrática Ln x", fontweight="bold")
plt.plot(x,fx, "ro", label= "Ln(x) Discreto")        #Valores dispersion
plt.plot(x,v_interpol_cua, label=u"Interpolación Cuadrática", lw=1.5)          #Interpolacion lineal
plt.plot(v_ep,fep, label=u"Ln(x) Original", lw=1.5)
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()

print v_interpol_cua