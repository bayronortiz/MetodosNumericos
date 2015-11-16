#-*-coding:utf-8 -*-

'''
	Descripción: Ejercicio 9.7, Usando el método gráfico para resolver el sistema ecuaciones dado,
				 determinante y eliminación de incognitas.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

from matplotlib import pyplot as plt
import numpy as np
from opermat import *

# Definimos las funciones originales
# f1 sistema lineal 0.5X1 - X2 = -9,5
f1 = lambda x1,x2: 0.5 * x1 - x2
# f2 sistema lineal 1.02X1 - 2X2 = -18.8
f2 = lambda x1,x2: 1.02 * x1 - 2 *x2

#Definimos las funciones despejadas para la gráfica
# Despejando x2 en f1
f1_d = lambda x1: (-9.5 - 0.5 * x1) / -1.0
# Despejando x2 en f2
f2_d = lambda x1: (-18.8 - 1.02 * x1) / -2.0

#Inicio del Programa
print "Sistema Ecuaciones Dado: "
print "0.5X1 - X2 = -9.5\n1.02X1 - 2X2 = -18.8"

print "\n", "#", "-" * 24, " a) Solución Por Medio del Método Gráfico ", "-" * 24, "#"
#Usando métod gráfico, obtenemos los valores
val_f1 = []
val_f2 = []
x = []

for i in range(0,20):
	x.append(i)
	val_f1.append(f1_d(i))
	val_f2.append(f2_d(i))

#Encuentra los valores donde se interceptan las gráficas
for i in range(0,len(x)):
	if round(val_f1[i], 2) == round(val_f2[i], 2):
		x1, x2 = (x[i], val_f2[i])
		break

print "\nLas Soluciones son: "
print "X1= ", x1, "\tX2= ", x2
print "\nSustituyendo Valores Tenemos: "
print "0.5(%.2f) - (%.2f) = %.2f" % (x1, x2, f1(x1,x2))
print "1.02(%.2f) - 2(%.2f) = %.2f" % (x1, x2, f2(x1,x2))

#Graficando los sistemas
plt.figure(u"Solución Gráfica Ej_9,7")
plt.title(u"Solución Gráfica")
gf1, = plt.plot(x,val_f1, label="0.5X1 - X2 = -9.5")
gf2, = plt.plot(x,val_f2, label="1.02X1 - 2X2 = -18.8")
plt.legend(handles= [gf1,gf2])
plt.grid(True)
plt.show()
print "\n#", "-" * 92, "#"

print "\n#", "-" * 33 , " b) Determinante Matriz ", "-" * 33 , "#"
op = OperMat()		#Objeto operaciones con matrices
M = np.array([[0.5, -1],[1.02, -2]], dtype=np.float64)
d = op.det(M)

print "\nMatriz Coeficientes [M]:"
print M
print "\nDeterminante/det(M)= ", d
print "\n#", "-" * 92, "#"

print "\n#", "-" * 29, " d) Resolviendo por Gauss Simple ", "-" * 28, "#"
A = np.array([[0.5, -1, -9.5],[1.02, -2, -18.8]], dtype= np.float64)  #Matriz Aumentada del sistema
X = op.gauss_simple(A)		#Calcula las incognitas del sistema gauss_simple

print "\nMatriz Aumentada del Sistema [A]:"
print A
print "\nIncognitas del Sistema: "
print "X1= %.2f\tX2= %.2f" % (X[0], X[1])
print "\n#", "-" * 92, "#"
