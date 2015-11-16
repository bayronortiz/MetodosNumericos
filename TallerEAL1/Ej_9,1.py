# -*-coding:utf-8 -*-

'''
	Descripción: Ejercicio 9.1, escribe la transpuesta del sistema de ecuaciones dado.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np
from opermat import *

print "\nSistema de Ecuaciones:"
print "50 = 5X3 + 2X2"
print "10-X1 = X3"
print "3X2 + 8X1 = 20"

print "\na) Forma Matricial Coeficientes (Matriz Aumentada):"
M = np.array([[0, 2, 5, 50], [-1, 0, -1, -10], [8, 0, 3, 20]])
print M

print "\nb) Transpuesta Matriz Coeficientes"
op = OperMat()
T = op.transpuesta(M)
print T
