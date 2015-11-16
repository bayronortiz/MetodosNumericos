#-*-coding:utf-8 -*-

'''
	Descripción: Ejercicio 9.5, Usando el método gráfico para resolver el sistema ecuaciones dado,
			     determinante y solución por método de gauss.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

from matplotlib import pyplot as plt
import numpy as np
from opermat import *

# Definimos la funcion1 original -1.1X1 + 10X2 = 120
def f1(x1, x2):
	return -1.1 * x1 + 10 * x2

# Definimos la funcion2 original -2X1 + 17.4X2 = 174
def f2(x1, x2):
	return -2 * x1 + 17.4 * x2

# Define la función -1.1X1 + 10X2 = 120 despejando X2
# X2 = (120 + 1.1X1) / 10
def f1_d(x1):
	return (120 + 1.1 * x1) / 10.0

# Define la función -2X1 + 17.4X2 = 174 despejando X2
# X2 = (174 + 2X1) / 17.4
def f2_d(x1):
	return (174 + 2 * x1) / 17.4


#Inicio del Programa
print "Sistema Ecuaciones Dado: "
print "-1.1X1 + 10X2 = 120\n-2X1 + 17.4X2 = 174"

#Matriz de Coeficientes
M = np.array([[-1.1, 10], [-2, 17.4]])
A = np.array([[-1.1, 10, 120],[-2, 17.4, 174]])		# Matriz Aumentada del sistema de ecuaciones

# Usando método gráfico, tenemos lo siguiente
val_f1 = []
val_f2 = []
x = []

#Asignamos los valores
for i in range(300,500):
	x.append(i)
	val_f1.append(f1_d(i))
	val_f2.append(f2_d(i))

#Encuentra los valores donde se interceptan las gráficas
for i in range(0,len(x)):
	if round(val_f1[i], 2) == round(val_f2[i], 2):
		x1, x2 = (x[i], val_f2[i])
		break

print "\n", "#", "-" * 24, " a) Solución Por Medio del Método Gráfico ", "-" * 24, "#"
print "\nLas Soluciones son: "
print "X1= ", x1, "\tX2= ", x2
print "\nSustituyendo Valores Tenemos:"
print "-1.1(%.1f) + 10(%.1f) = %.1f" % (x1, x2, f1(x1, x2))
print "-2(%.1f) + 17.4(%.1f) = %.1f" % (x1, x2, f2(x1, x2))

# Graficamos los dos sistemas
plt.figure(u"Solución Gráfica Ej_9,5")
plt.title(u"Solución Gráfica")
gf1, = plt.plot(x,val_f1, label="-1.1X1 + 10X2 = 120")
gf2, = plt.plot(x,val_f2, label="-2X1 + 17.4X2 = 174")
plt.legend(handles= [gf1,gf2])
plt.grid(True)
plt.show()
print "\n#", "-" * 92, "#"

print "\n#", "-" * 33 , " c) Determinante Matriz ", "-" * 33 , "#"
op = OperMat()  #Objeto de tipo OperarMatrices, contiene la función det(A)
print "\nMatriz Coeficientes [M]:"
print M,"\n"
print "Determinante/det(M)=", op.det(M)
print "\n#", "-" * 92, "#"

print "\n#", "-" * 29, " d) Resolviendo por Gauss Simple ", "-" * 28, "#"
print "\nMatriz Aumentada del Sistema [A]:"
print A
X = op.gauss_simple(A)		#Calcula las incognitas del sistema
print "\nIncognitas del Sistema:"
print "X1= %f\tX2= %f" % (X[0], X[1])
print "\n#", "-" * 92, "#"
