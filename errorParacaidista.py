# -*-coding: utf-8 -*-
# Fecha: 25-Ago-2015
# Calcula el Error Verdadero entre una solucion analitica y solucion aproximada

from math import *
import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt


n= input("Ingrese Cifras Significativas (n)--> ")  # n son cifras significativas

Es= 0.5*10**(2-n)  # Error tolerado/aceptable

vel_act= 0      # Velocidad actial ti+1
vel_ant= 0      # Velocidad anterior ti
sol_analitica= 0   # Valor verdadero
sol_aprox= 0      # Valor aproximado
Et= 0      # Error verdadero
t= 0
t_ant= 0           # Iteraciones

m= 68.1     #Constante masa
c= 12.5    # Constante coeficiente friccion
g= 9.8     # Constante gravedad

valores_analitica= []  #lista vacia, guarda los valores del calculo analitico
valores_aprox= []  #lista vacia, guarda los valores del calculo aproximado

print "\nError Tolerado: ",Es,"%"  # Imprime error tolerado
print "\nt | Sol Analitica | Sol Aproximado | Error\n"   #Convencion tabla

while True:
    sol_analitica= ((g*m)/c) * (1-exp(-(c/m)*t))     #Calcula la solucion analitica
    vel_act= vel_ant + (g-(c/m)*vel_ant) * (t - t_ant)  # Calcula la solucion aprox
    
    valores_analitica.append(sol_analitica)     #Agrega valores analiticos a la lista valores analitica
    valores_aprox.append(vel_act)       #Agrega valores aproximados a la lista valores_aprox

    vel_ant= vel_act
    sol_aprox= vel_act

    Et= abs( sol_analitica - sol_aprox)

    print "%d | %f | %f | %f\n" %(t, sol_analitica, sol_aprox, Et) #Impresion tabla

    if Et < Es and t != 0:  # Condición para terminar ciclo
        break

    t_ant= t
    t+=1        # Incrementa la variable tiempo
    
# Grafica de la solucion analitica y la solucion aproximada
sol_analitica,= plt.plot(valores_analitica,"b-", label="Sol. Analitica")
sol_aprox,= plt.plot(valores_aprox,"r-", label= "Sol. Aproximada")
plt.legend(handles=[sol_analitica, sol_aprox], loc= 4)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)
plt.show()
    
    
