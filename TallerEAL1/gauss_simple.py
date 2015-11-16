# -*-coding:utf-8 -*-

'''
	Descripción: Implementa la eliminación de guass simple hacia adelante y
				 sustitución hacia atrás.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np

# Sistema de ecuaciones lineales propuesto en el ejercicio
A = np.array([[3, -0.1, -0.2, 7.85], [0.1, 7, -0.3, -19.3], [0.3, -0.2, 10, 71.4]])
X = np.zeros((3,1))

print "Sistema Ecuaciones Propuesto:"
print "Matriz A:"
print A, "\n"

# Algoritmo de eliminación de Gauss Simple Hacia Adelante
#m, n = A.shape	#Obtenemos la dimension de la Matriz mxn
#print m,"x",n
n = 3  # N° de incognitas debe ser igual a el número de ecuaciones

# Eliminación de Gauss Simple hacia adelante
for k in range(0, n-1):
	for i in range(k+1, n):
		factor = A[i,k] / (A[k,k] * 1.0)
		for j in range(k,n):
			A[i,j] = A[i,j] - factor * A[k,j]
		A[i,n] = A[i,n] - factor * A[k,n]


# Sustitución hacia atrás
X[n-1] = A[n-1,n] / (A[n-1,n-1] * 1.0)

for i in range(n-1,-1,-1):
	sum = A[i,n]
	for j in range(i+1, n):
		sum = sum - A[i,j] * X[j]
	X[i] = sum / (A[i,i] * 1.0)		


print "\n\n#---------- Resultados: ----------# "
print "Matriz A:"
print A

print "\nIncognitas:"
print X
