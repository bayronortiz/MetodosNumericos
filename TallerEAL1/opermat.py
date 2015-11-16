# -*-coding:utf-8 -*-

'''
	Descripción: Clase que implementa las operaciones matematicas básicas de
				 matrices.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

import numpy as np

# Clase OperMat (Operaciones Matrices) define suma, diferencia, producto, traza utilizando matrices.
class OperMat():

	#Compara el tamaño de dos matrices. return-> true:iguales | ->false:diferentes
	#param:(Mat1:Matriz1, Mat2:Matriz2)													
	def comparar_tam(self, Mat1, Mat2):
		if Mat1.shape == Mat2.shape:
			return True
		else:
			return False
	

	# Suma de dos matrices, return->Mat | return->None
	# param:(Mat1:Matriz1, Mat2:Matriz2)
	def suma(self, Mat1, Mat2):
		if self.comparar_tam(Mat1,Mat2):
			m,n = Mat1.shape		#Obtenemos el tamaño de la matriz
			T = np.zeros((m,n))		#Creamos una matriz ceros, T:Temporal

			for i in range(0,m):		#Ralizamos la suma de las matrices
				for j in range(0,n):
					T[i,j] = Mat1[i,j] + Mat2[i,j]
			
			return T	#Retornamos el resultado
		else:
			return None		#Retorna Null, no es posible realizar la suma
	

	# Diferencia de dos matrices, return->Mat | return->None
	# param:(Mat1:Matriz1, Mat2:Matriz2)
	def diferencia(self, Mat1, Mat2):
		if self.comparar_tam(Mat1,Mat2):
			m,n = Mat1.shape		#Obtenemos el tamaño de la matriz
			T = np.zeros((m,n))		#Creamos una matriz ceros, T:Temporal

			for i in range(0,m):		#Ralizamos la diferencia de las matrices
				for j in range(0,n):
					T[i,j] = Mat1[i,j] - Mat2[i,j]
			
			return T	#Retornamos la matriz resultante
		else:
			return None		#Retorna Null, no es posible realizar la diferencia
	

	#Producto por escalar cMat, return->cMat
	#param:(c:Escalar, Mat:Matriz)
	def producto_c(self, c, Mat):
		m, n = Mat.shape		#Obtenemos las dimensiones de la matriz
		T = np.zeros((m,n))    # Creamos una matriz de ceros temporal

		for i in range(0, m):
			for j in range(0, n):
				T[i,j] = Mat[i,j] * c		#Multiplicamos por el escalar dado

		return T		#Devolvemos la matriz resultante

	
	# Producto de dos matrices, return->Mat | return->None
	# param:(Mat1: Matriz1, Mat2:Matriz2)
	def producto(self, Mat1, Mat2):
		m1, n1 = Mat1.shape		#Obtenemos dimensiones Matriz1
		m2, n2 = Mat2.shape		#Obtenemos dimensiones Matriz2
	
		if n1 == m2:
			T = np.zeros((m1,n2))
			r = n1		
			for i in range(0, m1):
				for j in range(0, n2):
					suma = 0		#Guarda temporalmente la suma de los productos fila x columna
					for k in range(0, r):
						suma += Mat1[i,k] * Mat2[k,j]
					T[i,j] = suma		# Asignamos el valor de los productos
							
			return T	#Retorna el resultado producto
		else:
			return None			#Retorna Null, no es posible realizar producto


	#Traza de una matriz(solo matrices cuadradas), return->SumaDiagonal:numeric | return->None
	#param:(Mat:Matriz)
	def tr(self, Mat):
		m, n = Mat.shape  #Obtengo el tamanio de la matriz

		if m == n:		#Verifica que la matriz sea cuadrada
			traza = 0
			for i in range(0, m):
				traza += Mat[i,i]		#Obtiene la traza de la matriz

			return traza
		else:
			return None

	
	# Define la transpuesta de una matriz, return->Mat
	# param:(Mat:Matriz)
	def transpuesta(self, Mat):
		m, n = Mat.shape		#Obtenemos el tamanio de la matriz m x n
		Mat_T = np.zeros((n, m))	#Creamos la matriz transpuesta de zeros de tamanio n x m

		for i in range(0, m):
			for j in range(0, n):
				Mat_T[j,i] = Mat[i,j]

		return Mat_T	#Retornamos el resultado
		
	
	# Metodo utilitario interno que busca si la matriz es cuadrada
	def _es_cuadrada(self, Mat):
		m, n = Mat.shape
		if m == n:
			return True
		else:
			return False


	# Determina el determinante de una matriz nxn
	# Intercambia fila pivote que contenga un cero. Evitar division por cero
	def _intercambia_fila(self, Mat, f1, f2):
		temp = 0
		n = Mat.shape[1]	#Columnas de la matriz

		for j in range(0, n):
			temp = Mat[f1,j]
			Mat[f1,j] = Mat[f2,j]
			Mat[f2,j] = temp
		

	# Método que devuelve el determinante de la matriz nxn	
	def det(self, Mat):
		#Verificamos que la matriz es cuadrada. Sino retorna null
		if not self._es_cuadrada(Mat):
			return None

		T = np.copy(Mat)			# Asignamos una nueva variable T:Matriz Temporal
		s = 1		# Controla el cambio de signo al intercambiar filas. s:signo
		p = 0		# Guarda cambios de filas p=0: no hay cambios
		n = T.shape[0]		#Obtengo las filas de la matriz. Matriz cuadrada nxn
		d = 1		# d:determinante, matriz que guarda el determinante 
		f = 0		# variable proposito general f:filas 
		c = 0		# variable proposito general c:columnas
		pivote = 0		#Guarda el valor de pivote
		temp = 0		#Variable proposito general auxiliar/temporal

		for i in range(0, n):
			p = 0
			if T[i,i] == 0:
				p = -1
				f = i
				while f < n and p == -1:
					if T[f,i] != 0:
						p = f
						self._intercambia_fila(T, i, p)
						s *= -1
					f += 1

			pivote = T[i,i]
			if p != -1:
				for f in range(i+1, n):
					temp = T[f,i]
					for c in range(0, n):
						T[f,c] = T[f,c] - (T[i,c] * (temp / (pivote * 1.0)))
			
		for i in range(0, n):
			d *= T[i,i] 
		d *= s

		return d


	# Función que implementa el método gauss simple para resolución de sistema de ecuaciones
	# Param: (Mat:numpy.array)
	# Return: Mat:Incognitas iguales a ecuaciones | Null: Si el # Ecuaciones es distinto al de incognitas
	def gauss_simple(self, Mat):
		# Algoritmo de eliminación de Gauss Simple Hacia Adelante
		#m, n = A.shape	#Obtenemos la dimension de la Matriz mxn
		#print m,"x",n
		n = Mat.shape[0]   # N° de incognitas debe ser igual a el número de ecuaciones

		if n+1 != Mat.shape[1]:
			return None

		A = np.copy(Mat)
		X = np.zeros((n,1))	# Creamos la matriz que guarda las incognitas

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
		
		return X		# Retornamos las incognitas

		
