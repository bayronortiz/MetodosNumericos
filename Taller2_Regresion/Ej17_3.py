#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.3, calculos estadisticos e histograma

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

#librerias
from reg_lineal import *
import matplotlib.pyplot as plt
import numpy as np

datos = [28.65, 26.55, 26.65, 27.65, 27.35, 28.35, 26.85,
         28.65, 29.65, 27.85, 27.05, 28.25, 28.35, 26.75,
         27.65, 28.45, 28.65, 28.45, 31.65, 26.35, 27.75,
         29.25, 27.65, 28.65, 27.65, 28.55, 27.55, 27.25]

calc = RegLineal()    #Objeto de tipo RegLineal, contiene operaciones estadisticas y regresion

# Imprime los resultados
print "*"*10, "Ejercico 17.3","*"*10
print "Datos:"
print "\t",datos
print "\nResultados:"
print "\tMedia= ", calc.calc_media(datos)
print "\tDesv. Estandar= ", calc.desv_std(datos)
print "\tVarianza= ", calc.varianza(datos)
print "\tCoef. Variacion(%)= ", calc.cv(datos)

#Histograma de los datos
rango = np.arange(26, 32 + 0.5, 0.5)       #Configuramos el rango de los datos ini=26, fin=32, paso=0.5

plt.figure("Histograma Ej17_3")
plt.hist(datos,rango, facecolor='green', alpha=0.8)
plt.title("Histograma Datos", fontweight="bold")
plt.xlabel("Rango (26 - 32)",fontweight="bold")
plt.ylabel("Frec. Acumulada",fontweight="bold")
plt.margins(x=.01,y=.01)
plt.subplots_adjust(left=0.15)
plt.grid(True)
plt.show()