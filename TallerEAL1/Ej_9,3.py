# -*-coding:utf-8 -*-

'''
	Descripción: Desarrollo Ejercicio 9.3, Producto entre matrices. Taller EAL_1
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np
from opermat import *

# Funcion de caracter estetico impresion en pantalla
def asteriscos():
	print "\n\n", "* " * 4


#Inicio del Programa
# Se definen las tres matrices siguientes
A = np.array([[1, 6], [3, 10], [7, 4]])
B = np.array([[1, 3], [0.5, 2]])
C = np.array([[2, -2], [-3, 1]])
op = OperMat()		#Objeto que contiene las operaciones basicas con matrices

print "\nSe Definen 3 Matrices con Dimensiones:"
print "[A]: ",A.shape[0], " x ", A.shape[1] 
print A
print "\n[B]: ", B.shape[0], " x ", B.shape[1]
print B
print "\n[C]: ", C.shape[0], " x ", C.shape[1]
print C
print "\n#", "-" * 92, "#\n"

print "Productos Posibles: AB / AC / BC / CB"
print "-Producto AB:"
print "[A]:"
print A
print "\n[B]:"
print B
print "\n[A] x [B]= "
print op.producto(A, B)

asteriscos()
print "-Producto AC:"
print "[A]:"
print A
print "\n[C]:"
print C
print "\n[A] x [C]= "
print op.producto(A, C)

asteriscos()
print "-Producto BC:"
print "[B]:"
print B
print "\n[C]:"
print C
print "\n[B] x [C]="
print op.producto(B, C)

asteriscos()
print "-Producto CB:"
print "[C]:"
print C
print "\n[B]:"
print B
print "\n[C] x [B]="
print op.producto(C, B)
