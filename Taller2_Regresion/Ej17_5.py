#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.5, Grafico Regresión Lineal, coeficiente
                 correlación y error estándar estimado.

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

#librerias
from reg_lineal import *
import matplotlib
matplotlib.use('Qt4Agg')   # Usa por defecto Qt4 para Gráficas. Lineal opcional
import matplotlib.pyplot as plt

# Datos de la tabla
x = [6, 7, 11, 15, 17, 21, 23, 29, 29, 37, 39]
y = [29, 21, 29, 14, 21, 15, 7, 7, 13, 0, 3]

op = RegLineal()    # Objeto con métodos para cálculo regresión lineal
recta = []    # lista vacía, guarda los datos de la recta regresión
a0 = op.calc_a0(x, y)    # Calcula el coeficiente a0
a1 = op.calc_a1(x, y)    # Calcula el coeficiente a1
r = op.calc_r(x, y)    # Calcula el coeficiente de correlación
error = op.error_std(x, y)  # Calcula el error estandar del estimado

print "\nResultados: "
print "Coeficientes:"
print "\ta0= %.4f\ta1= %.4f" % (a0, a1)
print "\t(Coef. Correlación) r= %.4f" % r
print "Ecuación Recta:"
print "\ty = %.4f + (%.4f)X" % (a0, a1)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error

for xi in x:
    temp = a0 + a1 * xi    # Damos los valores para la recta de regresión
    recta.append(temp)

# Gráfica Regresión Lineal
plt.figure(u"Gráfica Regresión X")
plt.title(u"Recta Regresión Lineal", fontweight="bold")
plt.plot(x, y, "ro", label= "Valores X")       # Valores dispersión
plt.plot(x, recta, label=u"Recta Regresión", lw=1.5)      # Recta de regresión
plt.xlabel("Valores X", fontweight="bold")
plt.ylabel("Valores Y", fontweight="bold")
plt.legend(loc=1)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()