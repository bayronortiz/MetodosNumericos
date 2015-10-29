# -*- coding:utf-8 -*-

'''
	Graficar funciones.
	Sin Solucion.
	Infinitas Soluciones.
	Mal condicionado.

    Elaborado Bayron Danilo Ortiz Foronda
'''


from math import *
from matplotlib import pyplot as plt

def sin_solucion():
	v1 = []
	v2 = []

	for i in range(10):
		v1.append(1 + (i / 2.0))
		v2.append((1.0 / 2.0) + (i / 2.0))
	
	plt.plot(v1)
	plt.plot(v2)
	plt.grid(True)
	plt.show()
	

def infinito_sol():
	v1 = []
	v2 = []

	for i in range(10):
		v1.append(1 + (i / 2.0))
		v2.append(1 + (i / 2.0))
	
	plt.plot(v1)
	plt.plot(v2)
	plt.grid(True)
	plt.show()


def mal_condicionado():
	v1 = []
	v2 = []

	for i in range(10):
		v1.append(1.1 + (2.3 / 5.0)*i)
		v2.append(1 + (1.0 / 2.0)*i)
	
	plt.plot(v1)
	plt.plot(v2)
	plt.grid(True)
	plt.show()



# Inicio del Programa
sin_solucion()
infinito_sol()
mal_condicionado()
