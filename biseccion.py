# -*- coding: utf-8 -*-

'''
    Cálcula la raíz de la función e^(-x) - x, usando el método de la bisección
    Elaborado: Bayron Ortiz
    Curso: Métodos Númericos
'''
import math

# Cálcula el valor en x de la Función Original
def funcion(x):
    return math.exp(-x) - x


# Funcion que calcula el cambio de signo de la funcion
# Param: inf(int): lim inferior -- sup(int):lim superior
# Return limites(int): tupla enteros
def limites(inf, sup):
    x = inf
    temp = 0

    while x <= sup:
        fx = funcion(x)

        if fx > 0:
            temp = x
        else:
            return (temp, x)

        x += 1


# Funcion que calcula el xr
def biseccion(xl, xu):
    i = 1
    xr = 0
    xr_ant = 0
    Ea = 0

    print "{0:3s} | {1:12s} | {2:12s} | {3:12s} | {4:12s}".format("It", "Xl", "Xu","Xr","Ea")

    while True:
        xr = (xl + xu) / 2.0
        Ea = abs((xr - xr_ant) / xr) * 100  #Calcula el error relativo porcentual
        
        print "{0:3d} | {1:.10f} | {2:.10f} | {3:.10f} | {4:.10f}".format(i, xl, xu, xr, Ea)

        condicion = funcion(xl) * funcion(xr)

        if condicion > 0:
            xl = xr
        elif condicion < 0:
            xu = xr
        else:
            break   # Deja de iterar cuando f(xl)*f(xr)==0

        xr_ant = xr
        i += 1


lim = limites(-20,20)   # Busca el cambio de signo de fx dentro de un rango -20,20
biseccion(lim[0], lim[1])  #Cálcula bisección de la funcion



