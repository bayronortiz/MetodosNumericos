# -*-coding:utf-8 -*-

'''
	Descripción: Código que implementa la media aritmetica y la desviacion
				 estandar de un conjunto de datos.
	Elaborado:	 Bayron Danilo Ortiz Foronda.
	Version Python: 2.7
'''

import math
import numpy as np

# Funcion para hallar media aritmetica
# param: datos:arreglo
# return: valor_media:int
def media_aritmetica(datos):
	valor_media = 0

	for i in datos:
		valor_media += i
	
	valor_media /= len(datos) * 1.0

	return valor_media

# Funcion que calcula la desviación estandar
# param: datos:arreglo, media:numerico,
# return: desv:numerico
def desviacion_std(datos, media):
	sumatoria = 0

	for i in datos:
		sumatoria += (i - media)**2
	
	desv = sumatoria / (len(datos)-1)

	return math.sqrt(desv)


# Inicio del Programa
datos = [19, 19, 23, 21, 21, 21, 19, 18, 20, 22, 22, 21, 19, 19, 20, 20, 20, 21, 20, 23]

print "\n::CALCULA LA MEDIA Y DESVIACIÓN ESTANDAR DE UN CONJUNTO DE DATOS::\n"
print "Datos:"
print datos

med= media_aritmetica(datos)
print "\nMedia Aritmetica (Formula):"
print "\tmed = ", med
print "Media Aritmetica (Numpy):"
print "\tmed_np = ", np.mean(datos)

print "\n\nDesviación Estandar (Formula):"
print "\tsd = ", desviacion_std(datos, med)
print "\nDesviación Estandar (Numpy):"
print "\tsd_np = ", np.std(datos)
