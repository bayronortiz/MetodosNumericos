#-*-coding:utf-8 -*-

'''
	Descripción: Desarrollo Ejercicio 9,2 propuesto en taller EAL_1. Operaciones con matrices.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''


from opermat import *

# Funciones de Impresion/Presentacion. Nada que ver con la lógica del programa 
def asteriscos():
	print "\n\n", "* " * 4

# Verifica que T es diferente de Null, en tal caso muestra mensaje
def verificar_T(T):
	if T is None:
		return "No Esta Definida"
	else:
		return T


# Inicio del Programa
# Creamos las matrices
A = np.array([[4,7],[1,2],[5,6]])
B = np.array([[4,3,7],[1,2,7],[1,0,4]])
C = np.array([[3],[6],[1]])
D = np.array([[9,4,3,-6],[2,-1,7,5]])
E = np.array([[1,5,8],[7,2,3],[4,0,6]])
F = np.array([[3,0,1],[1,7,3]])
G = np.array([[7,6,4]])

# Mostramos en pantalla c/u de las matrices
print "#", "-" * 40, " MATRICES ", "-" * 40, "#"
print "-Matriz A:"
print A
print "\n-Matriz B:"
print B
print "\n-Matriz C:"
print C
print "\n-Matriz D:"
print D
print "\n-Matriz E:"
print E
print "\n-Matriz F:"
print F
print "\n-Matriz G:"
print G
print "\n#", "-" * 92, "#\n"

# Punto a) Mostramos las dimensiones de la matrices
print "#","-" * 29, " a) Dimensiones de las Matrices ", "-" * 29, "#"
print "-Matriz A: ", A.shape[0], " x ", A.shape[1]
print A
print "\n-Matriz B: ", B.shape[0], " x ", B.shape[1]
print B
print "\n-Matriz C: ", C.shape[0], " x ", C.shape[1]
print C
print "\n-Matriz D: ", D.shape[0], " x ", D.shape[1]
print D
print "\n-Matriz E: ", E.shape[0], " x ", E.shape[1]
print E
print "\n-Matriz F: ", F.shape[0], " x ", F.shape[1]
print F
print "\n-Matriz G: ", G.shape[0], " x ", G.shape[1] 
print G
print "\n#", "-" * 92, "#\n"

# Punto b) Identificar matriz cuadrada, columna y renglón
print "#", "-" * 26, " b) Matriz Cuadrada, Columna y Renglón ", "-" * 25, "#"
print "Matriz CUADRADA:"
print "Matriz B:"
print B
print "\nMatriz E:"
print E
print "\nMatriz COLUMNA:"
print "Matriz C:"
print C
print "\nMatriz RENGLÓN:"
print "Matriz G:"
print G
print "\n#", "-" * 92, "#\n"

# Punto c) Valores de los elementos a12, b23, d32, e22, f12, g12
print "#", "-" * 19, " c) Valores Elementos a12, b23, d32, e22, f12 y g12 " ,"-" * 19, "#"
print "-Matriz A:"
print A
print "Elemento a12= ", A[1-1,2-1]
print "\n-Matriz B:"
print B
print "Elemento b23= ", B[2-1,3-1]
print "\n-Matriz D:"
print D
print "Elemento d32= No Existe. Sobrepasa limites de la matriz." 
print "\n-Matriz E:"
print E
print "Elemento e22= ", E[2-1,2-1]
print "\n-Matriz F:"
print F
print "Elemento f12= ", F[1-1,2-1]
print "\n-Matriz G:"
print G
print "Elemento g12= ", G[1-1,2-1]
print "\n#", "-" * 92, "#\n"

# Punto d) Diferentes Operaciones Entre Matrices
op = OperMat()
print "#", "-" * 37, " d) Operaciones ", "-" * 37, "#"
print "1) [E] + [B]:"
print "[E]"
print E
print "\n[B]"
print B
print "\n[E] + [B]="
T = op.suma(E, B)
print verificar_T(T)

asteriscos()
print "2) [A] + [F]:"
print "[A]"
print A
print "\n[F]"
print F
print "\n[A] + [F]= "
T = op.suma(A, F)
print verificar_T(T)

asteriscos()
print "3) [B] - [E]:"
print "[B]"
print B
print "\n[E]"
print E
print "\n[B] - [E]= "
T = op.diferencia(B, E)
print verificar_T(T)

asteriscos()
print "4) 7 x [B]:"
print "[B]"
print B
print "\nEscalar\n7"
print "\n7 x [B]="
print op.producto_c(7, B)

asteriscos()
print "5) [E] x [B]:"
print "[E]"
print E
print "\n[B]"
print B
print "\n[E] x [B]="
T = op.producto(E, B)
print verificar_T(T)

asteriscos()
print "6) {C}^T:"
print "{C}"
print C
print "\n{C}^T="
print op.transpuesta(C)

asteriscos()
print "7) [B] x [A]:"
print "[B]"
print B
print "\n[A]"
print A
print "\n[B] x [A]= "
T = op.producto(B, A)
print verificar_T(T)

asteriscos()
print "8) [D]^T:"
print "[D]"
print D
print "\n[D]^T="
print op.transpuesta(D)

asteriscos()
print "9) [A] x [C]:"
print "[A]"
print A
print "\n[C]"
print C
print "\n[A] x [C]="
T = op.producto(A, C)
print verificar_T(T)

asteriscos()
print "10) [I] x [B]:"
print "[I]"
I = np.identity((B.shape[0]))
print I
print "\n[B]"
print B
print "\n[I] x [B]= "
T = op.producto(I, B)
print verificar_T(T)

asteriscos()
print "11) [E]^T [E]:"
print "[E]^T"
Et = op.transpuesta(E)
print Et
print "\n[E]"
print E
print "\n[E]^T [E]="
T = op.producto(Et, E)
print verificar_T(T)

asteriscos()
print "12) {C}^T {C}:"
print "{C}^T"
Ct = op.transpuesta(C)
print Ct
print "\n{C}"
print C
print "\n{C}^T {C}="
T = op.producto(Ct, C)
print verificar_T(T)
print "\n#", "-" * 92, "#\n"
