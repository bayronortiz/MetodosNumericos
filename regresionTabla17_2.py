#-*-coding: utf-8 -*-

'''
    Descripción: Script genera dos gráficas de dispersion y calcula la recta de
                 la linea de regresión, de dos modelos matematicos.

	Elaborado:	 Bayron Danilo Ortiz Foronda.

	Version Python: 2.7
'''

import matplotlib.pyplot as plt
from reg_lineal import *
import math

# Constantes globales
M = 68.1        # Masa del paracaidista
C = 12.5        # Coeficiente de arrastre
G = 9.8         # Constante gravitacional

#Funciones Lambda que definen el modelo1 y modelo2y
model1 = lambda t:((G * M) / C) * (1 - math.exp((-C / M) * t))
model2 = lambda t:((G * M) / C) * (t / (3.75 + t))

vel_medida = [10.0,16.30,23.0,27.5,31.0,35.6,39.0,41.50,42.9,45.0,46.0,45.50,46.0,49.0,50.0]
t = range(1,16)  # Definimos el arreglo t consecutivo 1-15
v_model1 = []   #Valores de model1
v_model2 = []   #Valores de model2
recta1 = []     # Recta modelo 1
recta2 = []     # Recta modelo 2
recta1_med = []     #recta regresion modelo1 vs vel medida
recta2_med = []     #recta regresion modelo2 vs vel medida
a0_m1 = 0       # Guarda el coeficiente a0 modelo1
a1_m1 = 0       # Guarda el coeficiente a1 modelo1
a0_m2 = 0       # Guarda el coeficiente a0 modelo2
a1_m2 = 0       # Guarda el coeficiente a1 modelo2
a0_med_m1 = 0       #Guarda coeficiente a0 velocidad medida vs modelo1
a1_med_m1 = 0       #Guarda coeficiente a1 velocidad medida vs modelo1
a0_med_m2 = 0       #Guarda coeficiente a0 velocidad medida vs modelo2
a1_med_m2 = 0       #Guarda coeficiente a1 velocidad medida vs modelo2
op_reg = RegLineal()        # Objeto de tipo regresión lineal para encontrar coeficientes

# Obtenemos los valores de las funciones para cada t
for i in t:
    v_model1.append(model1(i))
    v_model2.append(model2(i))

# obtenemos la pendiente a1 y el puto de corte a0
a1_m1 = op_reg.calc_a1(t, v_model1)
a0_m1 = op_reg.calc_a0(t, v_model1)
a1_m2 = op_reg.calc_a1(t, v_model2)
a0_m2 = op_reg.calc_a0(t, v_model2)

for i in t:
    recta1.append(a0_m1 + a1_m1 * i)
    recta2.append(a0_m2 + a1_m2 * i)

print "\nGRAFICO DISPERSION Y RECTA REGRESIÓN"
print "Modelo 1:"
print "\ta0= %.4f\ta1= %.4f"%(a0_m1, a1_m1)
print "\nModelo 2:"
print "\ta0= %.4f\ta1= %.4f"%(a0_m2, a1_m2)

# Graficamos modelo dispersion y la recta de regresión modelo1
plt.figure(u"Gráfica Regresión Modelo 1")
plt.title(u"Regresión Lineal Modelo 1", fontweight="bold")
plt.plot(t, v_model1, "ro", label= "Velocidad Modelo 1")        #Valores dispersion
plt.plot(t, recta1, label=u"Recta Regresión", lw=1.5)          #Recta de regresión
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)

# Graficamos modelo dispersion y la recta de regresión modelo2
plt.figure(u"Gráfica Regresión Modelo 2")
plt.title(u"Regresión Lineal Modelo 2", fontweight="bold")
plt.plot(t, v_model2, "ro", label= "Velocidad Modelo 2")        #Valores dispersion
plt.plot(t, recta2, label=u"Recta Regresión", lw=1.5)          #Recta de regresión
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()

# Calcula c/u de los coeficientes modelo vs vel medida
a1_med_m1 = op_reg.calc_a1(vel_medida, v_model1)
a0_med_m1 = op_reg.calc_a0(vel_medida, v_model1)
a1_med_m2 = op_reg.calc_a1(vel_medida, v_model2)
a0_med_m2 = op_reg.calc_a0(vel_medida, v_model2)

for i in vel_medida:
    recta1_med.append(a0_med_m1 + a1_med_m1 * i)
    recta2_med.append(a0_med_m2 + a1_med_m2 * i)

#Hallamos los coeficientes de correlación
r1 = op_reg.calc_r(vel_medida, v_model1)
r2 = op_reg.calc_r(vel_medida, v_model2)

print "\n"
print "-"*80
print "\nVel Medida vs Modelo 1:"
print "\ta0= %.4f\ta1= %.4f"%(a0_med_m1, a1_med_m1)
print "\t(Coeficiente Correlación) r= %.4f"%(r1)
print "\nVel Medida vs Modelo 2:"
print "\ta0= %.4f\ta1= %.4f"%(a0_med_m2, a1_med_m2)
print "\t(Coeficiente Correlación) r= %.4f"%(r2)

# Graficamos el modelo de dispersion velocidad Media vs Modelo 1
plt.figure(u"Gráfica Regresión V. Medida vs Modelo 1")
plt.title(u"Regresión Lineal Vel Medida vs Modelo 1", fontweight="bold")
plt.plot(vel_medida, v_model1, "ro", label= "Vel Modelo 1")        #Valores dispersion
plt.plot(vel_medida, recta1_med, label=u"Recta Regresión", lw=1.5)          #Recta de regresión
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)

# Graficamos el modelo de dispersion velocidad Media vs Modelo 1
plt.figure(u"Gráfica Regresión V. Medida vs Modelo 2")
plt.title(u"Regresión Lineal Vel Medida vs Modelo 2", fontweight="bold")
plt.plot(vel_medida, v_model2, "ro", label= "Vel Modelo 2")        #Valores dispersion
plt.plot(vel_medida, recta2_med, label=u"Recta Regresión", lw=1.5)          #Recta de regresión
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()
