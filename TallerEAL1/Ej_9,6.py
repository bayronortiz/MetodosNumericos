#-*-coding:utf-8 -*-

'''
	Descripción: Ejercicio 9.6, calcular determinante del sistema ecuaciones y encuentra los valores
				 de las incognitas usando gauss simple con sustitución hacia atrás.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np
from opermat import *

print "\nSistema de Ecuaciones dado:"
print "2X2 + 5X3 = 9\n2X1 + X2 + X3 = 9\n3X1 + X2 = 10"
M = np.array([[0,2,5],[2,1,1],[3,1,0]], dtype= np.float64)   #Matriz de coeficientes
B = np.array([[9],[9],[10]], dtype= np.float64)			# Matriz de resultados

print "\n#", "-" * 36, " a) Determinante: ", "-" * 35, "#"
op = OperMat()		#Objeto que contiene operaciones con matrices
print "\nMatriz Coeficientes [M]:"
print M
dg = op.det(M)		# Obtiene el determinante general del sistema ecuaciones
print "\nDeterminante (det(M))= ", dg
print "\n#", "-" * 92, "#"


print "\n#", "-" * 35, " b) Valor Incognitas ", "-" * 34, "#"
print "\nMatriz Coeficientes del Sistema [M]:"
print M
print "\nDeterminantes:"

m, n = M.shape		# Obtengo las dimensiones de la matriz mxn
det = []	#Lista para guardar c/u de los determinantes d1,d2,d3
for i in range(0, m):		# Hallando c/u de los determinante por regla de Cramer
	T = np.copy(M)
	for j in range(0, n):
		T[j,i] = B[j,0]
	
	print "\n","*" * 4
	print T
	det.append(op.det(T))
	print "\n\td%d= %.2f" % (i+1,det[i])
	det[i] /= dg


print "\nValores de Incognitas:"
print "X1= %.2f\tX2= %.2f\tX3= %.2f" % (det[0], det[1], det[2])
print "\n#", "-" * 92, "#"


print "\n#", "-" * 27, " c) Sustituyendo Valores Incognitas ", "-" * 27, "#"
print "\nSistema Ecuaciones:"
print "2X2 + 5X3 = 9\n2X1 + X2 + X3 = 9\n3X1 + X2 = 10"

print "\nValores de Incognitas:"
print "X1= %.2f\tX2= %.2f\tX3= %.2f" % (det[0], det[1], det[2])

print "\nSustituyendo: "
print "2(%.2f) + 5(%.2f) = %.2f" % (det[1], det[2], 2*det[1] + 5*det[2])
print "2(%.2f) + (%.2f) + (%.2f) = %.2f" % (det[0], det[1], det[2], 2*det[0] + det[1] + det[2])
print "3(%.2f) + (%.2f) = %.2f" % (det[0], det[1], 3*det[0]+ det[1])
print "\n#", "-" * 92, "#"

