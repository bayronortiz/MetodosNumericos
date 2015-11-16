#-*- coding:utf-8 -*-

'''
	Graficar funciones.
	Sin Solucion.
	Infinitas Soluciones.
	Mal condicionado.

    Elaborado Bayron Danilo Ortiz Foronda
'''


from math import *
from matplotlib import pyplot as plt
from matplotlib import gridspec


#Listas
s1 = []		#Lista valores funcion1 sin solucion
s2 = []		#Lista valores funcion2 sin solucion

i1 = []		#Lista valores funcion1 infinitas soluciones
i2 = []		#Lista valores funcion2 infinitas soluciones

m1 = []		#Lista valores funcion1 mal condicionado
m2 = []		#Lista valores funcion2 mal condicionado


# Funcion que calcula c/u de los valores de las funciones
def calcular_valores():
	for i in range(10):
		# Calcula valores s1 y s2  sin solucion
		s1.append(1 + (i / 2.0))
		s2.append((1 / 2.0) + (i / 2.0))

		# Calcula valores i1 y i2 infinitas soluciones
		i1.append(1 + (i / 2.0))
		i2.append(1 + (i / 2.0))

		#Calcula valores m1 y m2 mal condicionados
		m1.append(1.1 + (2.3 / 5) * i)
		m2.append(1 + (1 / 2.0) * i)


def graficar_funciones():
	valoresX = []
	
	for i in range(10):
		valoresX.append(i)
	
	fig = plt.figure("Tipos de Sistemas Lineales")
	gs = gridspec.GridSpec(3,1) #Cuadricula de 3 filas x 1 Columna
	
	# Grafica 1
	gf1 = fig.add_subplot(gs[0,0])
	plt.title(u"Sistema Sin Solución")
	f1, = gf1.plot(valoresX, s1, label="X2 = 1 + (X1/2)")
	f2, = gf1.plot(valoresX, s2, label="X2 = (1/2) + (X1/2)")
	gf1.legend(handles=[f1,f2], loc=4, fontsize="small")
	gf1.grid(True)

	#Grafica 2
	gf2 = fig.add_subplot(gs[1,0])
	plt.title("Sistema Infinitas Soluciones")
	f1, = gf2.plot(valoresX, i1, label="X2 = 1 + (X1/2)")
	f2, = gf2.plot(valoresX, i2, label="X2 = 1 + (X1/2)")
	gf2.legend(handles=[f1,f2], loc=4, fontsize="small")
	gf2.grid(True)

	# Grafica 3
	gf3 = fig.add_subplot(gs[2,0])
	plt.title("Sistema Mal Condicionado")
	f1, = gf3.plot(valoresX, m1, label="X2 = 1.1 + (2.3/5)*X1")
	f2, = gf3.plot(valoresX, m2, label="X2 = 1 + (X1/2)")
	gf3.legend(handles=[f1,f2], loc=4, fontsize="small")
	gf3.grid(True)

	plt.show()


# Inicio Programa
calcular_valores()	# Calcula los valores de c/u de las funciones
graficar_funciones()	#Muestra c/u de la funciones en pantalla
