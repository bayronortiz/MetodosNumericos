#-*-coding:utf-8 -*-

'''
	Descripción: Resuelve el ejercicio 9.8 por eliminación Gauss Simple.
				 Luego reemplaza los valores.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np


#Inicio del Programa	
# Sistema de ecuaciones lineales propuesto en el ejercicio
A = np.array([[10, 2, -1, 27], [-3, -6, 2, -61.5], [1, 1, 5, -21.5]])
X = np.zeros((3,1))

print "Sistema Ecuaciones Propuesto:"
print "\t10X1 + 2X2 -X3 = 27\n\t-3X1 -6X2 + 2X3 = -61.5\n\tX1 + X2 + 5X3 = -21.5"
print "\nMatriz Aumentada del Sistema:"
print "Matriz A:"
print A

# Algoritmo de eliminación de Gauss Simple Hacia Adelante
#m, n = A.shape	#Obtenemos la dimension de la Matriz mxn
#print m,"x",n
n = 3		# N° de incognitas debe ser igual a el número de ecuaciones

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


print "\n\n#", "-" * 31, "a) Eliminación Gauss Simple ", "-" * 31, "#"
print "Matriz A:"
print A

print "\nIncognitas:"
print X
print "\n#", "-" * 92, "#"

print "\n#","-" * 23, " b) Sustituir Incognitas en las Ecuaciones: ", "-" * 23 ,"#"
print "x1= %f\tx2= %f\tx3= %f"%(X[0], X[1], X[2])
print "\n10(%.1f) + 2(%.1f) -(%.1f) = %.1f" % (X[0], X[1], X[2], 10*X[0] + 2*X[1] - X[2]) 
print "-3(%.1f) - 6(%.1f) + 2(%.1f) = %.1f" % (X[0], X[1], X[2], -3*X[0] - 6*X[1] + 2*X[2])
print "%.1f + (%.1f) + 5(%.1f) = %.1f" % (X[0], X[1], X[2], X[0] + X[1] + 5*X[2])
print "\n#", "-" * 92, "#"
