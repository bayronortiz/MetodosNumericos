#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.4, Grafico Regresión Lineal y coeficiente
                 correlación

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

#librerias
from reg_lineal import *
import matplotlib
matplotlib.use('Qt4Agg')   # Usa por defecto Qt4 para Gráficas. Lineal opcional
import matplotlib.pyplot as plt
import numpy as np

x = [0, 2, 4, 6, 9, 11, 12, 15, 17, 19]
y = [5, 6, 7, 6, 9, 8, 7, 10, 12, 12]

consecutivo = np.arange(1, 11)    # Creamos el vector consecutivo de 1 hasta 10
recta_xy = []    # guarda los valores de la recta regresion x vs y
recta_x = []        # guarda los valores recta regresion para x
recta_y = []        # guarda los valores recta regresion para y

op_reg = RegLineal()    # Objeto que contiene los métodos para regresión lineal

a0_x = op_reg.calc_a0(consecutivo, x)      # a0 para x
a1_x = op_reg.calc_a1(consecutivo, x)        # a1 para x
error_x = op_reg.error_std(consecutivo, x)    # Error estandar estimado para x

a0_y = op_reg.calc_a0(consecutivo, y)    # a0 para y
a1_y = op_reg.calc_a1(consecutivo, y)        # a1 para y
error_y = op_reg.error_std(consecutivo, y)    # Error estandar estimado para y

a0_xy = op_reg.calc_a0(x, y)    # a0 para x vs y
a1_xy = op_reg.calc_a1(x, y)    # a1 para x vs y
error_xy = op_reg.error_std(x, y)    # Error estandar estimado para x vs y

for xi, c in zip(x, consecutivo):
    recta_xy.append(a0_xy + a1_xy * xi)
    recta_x.append(a0_x + a1_x * c)
    recta_y.append(a0_y + a1_y * c)

print "*" * 10, "Ejercicio 17.4", "*" * 10
# Regresión para x------------------------------------------------------------
print "\nRegresión Para X: "
print "\t(Consecutivo) c= ", consecutivo
print "\tx= ", x
print "Coeficientes:"
print "\ta0= %.4f\ta1= %.4f" % (a0_x, a1_x)
print "\t(Ecuación) y= %.4f + (%.4f) * x" % (a0_x, a1_x)
print "\t(Coeficiente Correlación) r= %.4f" % op_reg.calc_r(consecutivo, x)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_x
print "#", "-" * 80, "\n"

# Regresión para y------------------------------------------------------------
print "\nRegresión Para Y: "
print "\t(Consecutivo) c= ", consecutivo
print "\ty= ", y
print "Coeficientes:"
print "\ta0= %.4f\ta1= %.4f" % (a0_y, a1_y)
print "\t(Ecuación) y= %.4f + (%.4f) * x" % (a0_y, a1_y)
print "\t(Coeficiente Correlación) r= %.4f" % op_reg.calc_r(consecutivo, y)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_y
print "#", "-" * 80, "\n"

# Regresión para x vs y-------------------------------------------------------
print "\nRegresión Para X vs Y: "
print "\tx= ", x
print "\ty= ", y
print "Coeficientes:"
print "\ta0= %.4f\ta1= %.4f" % (a0_xy, a1_xy)
print "\t(Ecuación) y= %.4f + (%.4f) * x" % (a0_xy, a1_xy)
print "\t(Coeficiente Correlación) r= %.4f" % op_reg.calc_r(x, y)
print "Error Estándar Estimado: "
print "\tSyx= %.4f" % error_xy

# Gráfica de los datos y recta de regresión x
plt.figure(u"Gráfica Regresión X")
plt.title(u"Regresión Lineal X", fontweight="bold")
plt.plot(consecutivo, x, "ro", label= "Valores X")        # Valores dispersion
plt.plot(consecutivo, recta_x, label=u"Recta Regresión", lw=1.5)          # Recta de regresión
plt.xlabel("Consecutivo", fontweight="bold")
plt.ylabel("Valores X", fontweight="bold")
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()

# Gráfica de los datos y recta de regresión y
plt.figure(u"Gráfica Regresión Y")
plt.title(u"Regresión Lineal Y", fontweight="bold")
plt.plot(consecutivo, y, "ro", label= "Valores Y")        # Valores dispersion
plt.plot(consecutivo, recta_y, label=u"Recta Regresión", lw=1.5)          # Recta de regresión
plt.xlabel("Consecutivo", fontweight="bold")
plt.ylabel("Valores Y", fontweight="bold")
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()

# Gráfica de los datos y recta de regresión x vs y
plt.figure(u"Gráfica Regresión xy")
plt.title(u"Regresión Lineal x vs y", fontweight="bold")
plt.plot(x, y, "ro", label= "y")         # Valores dispersion
plt.plot(x, recta_xy, label=u"Recta Regresión", lw=1.5)    # Recta de regresión
plt.xlabel("Valores x", fontweight="bold")
plt.ylabel("Valores y", fontweight="bold")
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()
