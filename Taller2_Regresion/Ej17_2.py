#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.2 Histograma datos Ej17_1

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

import numpy as np
import matplotlib.pyplot as plt

# Datos Ejercicio 17.1
datos = [8.8,9.4,10,9.8,10.1,
         9.5,10.1,10.4,9.5,9.5,
         9.8,9.2,7.9,8.9,9.6,
         9.4,11.3,10.4,8.8,10.2,
         10,9.4,9.8,10.6,8.9]

rango = np.arange(7.5, 11.5 + 0.5, 0.5)       #Configuramos el rango de los datos ini=7.5, fin=11.5, paso=0.5

plt.figure("Histograma Ej17_2")
plt.hist(datos,rango, facecolor='green', alpha=0.8)
plt.title("Histograma Datos", fontweight="bold")
plt.xlabel("Rango (7.5 - 11.5)",fontweight="bold")
plt.ylabel("Frec. Acumulada",fontweight="bold")
plt.margins(y=.01,x=.01)
plt.subplots_adjust(left=0.15)
plt.grid(True)
plt.show()