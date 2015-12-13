#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.6, Grafico Regresión Lineal, coeficiente
                 correlación y error estándar estimado.

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

# librerias
from reg_lineal import *
import matplotlib
matplotlib.use('Qt4Agg')   # Usa por defecto Qt4 para Gráficas. Linea opcional
import matplotlib.pyplot as plt

# Datos
x = [2, 4, 6, 7, 10, 11, 14, 17, 20]
y = [1, 2, 5, 2, 8, 7, 6, 9, 12]

op = RegLineal()    # Objeto operaciones regresión lineal
a0 = op.calc_a0(x,y)
a1 = op.calc_a1(x,y)

# Gráfica Regresión Lineal
plt.figure(u"Gráfica Regresión X")
plt.title(u"Recta Regresión Lineal", fontweight="bold")
plt.plot(x, y, "ro", label= "Valores X")       # Valores dispersión
#plt.plot(x, recta, label=u"Recta Regresión", lw=1.5)      # Recta de regresión
plt.xlabel("Valores X", fontweight="bold")
plt.ylabel("Valores Y", fontweight="bold")
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()