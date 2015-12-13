#-*-coding:utf-8 -*-

'''
    Descripción: Ejercicio 17.1. Calculo de estadisticos.

    Elaborado:   Bayron Danilo Ortiz Foronda

    Python Ver. 2.7
'''

from reg_lineal import *        #Importamos clase RegLineal. Cotiene operaciones regresión y estadisticas

datos = [8.8,9.4,10,9.8,10.1,
         9.5,10.1,10.4,9.5,9.5,
         9.8,9.2,7.9,8.9,9.6,
         9.4,11.3,10.4,8.8,10.2,
         10,9.4,9.8,10.6,8.9]

calc = RegLineal()    #Objeto de tipo RegLineal, contiene operaciones estadisticas y regresion

# Imprime los resultados
print "*"*10, "Ejercico 17.1","*"*10
print "Datos:"
print "\t",datos
print "\nResultados:"
print "\tMedia= ", calc.calc_media(datos)
print "\tDesv. Estandar= ", calc.desv_std(datos)
print "\tVarianza= ", calc.varianza(datos)
print "\tCoef. Variacion(%)= ", calc.cv(datos)