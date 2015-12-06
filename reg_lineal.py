#-*-coding:utf-8 -*-

'''
    Descripción: Clase para el cálculo de las regresiones lineales.
    Elaborado:   Bayron Danilo Ortiz Foronda
    Python Ver. 2.7
'''

import math

# Definimos la clase que calcula los coeficientes a0 y a1, sumatorias.
# Para el cálculo de la regresión lineal
class RegLineal():
    # Función que calcula la sumatoria de una serie de datos
    # param: v_val:vector
    # return: sum:numerico
    def sumatoria(self,v_val):
        sum = 0     #Guarda el valor de la sumatoria

        for i in v_val:     #Sumamos c/u de los valores
            sum += i

        return sum      #Retornamos la suma


    #funcion que calcula la sumatoria de una serie de datos elevando c/u al cuadrado
    #param: v_val:vector numeros
    #return sum_cua:numerico
    def sumatoria_cua(self, v_val):
        sum_cua = 0

        for i in v_val:
            sum_cua += i ** 2

        return sum_cua


    #Funcion que calcula la sumatoria del producto de dos vectores
    #param: v_x:vector, v_y: vector
    #return: sum_xy: numeric float
    def sumatoria_xy(self, v_x, v_y):
        sum_xy = 0

        for xi, yi in zip(v_x, v_y):
            sum_xy += xi * yi

        return sum_xy


    # Función calcula la media de los datos
    # param: v_val:vector
    # return: media:numeric
    def calc_media(self,v_val):
        return self.sumatoria(v_val) / float(len(v_val))   # Devuelve la media de los datos


    # Función calcula la varianza muestral de los datos}
    #param: v_val: vector valores
    #return: var:numeric float
    def varianza(self, v_val):
        med = self.calc_media(v_val)
        _sum = 0
        var = 0

        for i in v_val:
            _sum += (i - med) ** 2

        var = _sum / float(len(v_val) - 1)

        return var        # retorna la varianza de los datos


    #Función calcula la desviación estandar muestral de los datos
    #param: v_val: vector valores
    #return: desv: numeric float
    def desv_std(self, v_val):
        desv = self.varianza(v_val)

        return math.sqrt(desv)


    #Función que calcula el Coeficiente Variación en Porcentaje (CV%)
    #param: v_val: vector datos
    #return: cv:float numeric %
    def cv(self, v_val):
        med = self.calc_media(v_val)    #Media
        sd = self.desv_std(v_val)    #desviacion estandar

        cv = (sd / med) * 100

        return cv


    # Función que calcula el coeficiente a1
    # param: v_x:vector, v_y:vector, v_xy:vector
    # return: a1:numeric
    def calc_a1(self,v_x, v_y):
        n = len(v_x)    # Tamanio
        sum_xy = self.sumatoria_xy(v_x, v_y)    #sumatoria xi*yi
        sum_x = self.sumatoria(v_x)      #sumatoria valores de x (consecutivo)
        sum_y = self.sumatoria(v_y)      #sumatoria valores de y (datos)
        sum_x_cua = self.sumatoria_cua(v_x)     #sumatoria de xi²

        a1 = ((n * sum_xy) - (sum_x * sum_y)) / float(((n * sum_x_cua) - (sum_x**2)))

        return a1


    # Función que calcula el coeficiente a0
    # param: v_x:vector, v_y:vector, a1:float
    # return a0:numeric
    def calc_a0(self,v_x, v_y):
        a1 = self.calc_a1(v_x, v_y)
        x_med = self.calc_media(v_x)
        y_med = self.calc_media(v_y)

        return float(y_med - a1 * x_med)


    #Funcion que calcula el coeficiente de correlación
    #param: v_x:vector, v_y:vector
    #return: r:numeric float
    def calc_r(self, v_x, v_y):
        n = len(v_x)
        sum_x = self.sumatoria(v_x)
        sum_y = self.sumatoria(v_y)
        sum_x_cua = self.sumatoria_cua(v_x)
        sum_y_cua = self.sumatoria_cua(v_y)
        sum_xy = self.sumatoria_xy(v_x, v_y)

        r = ((n * sum_xy) - (sum_x * sum_y)) / ((math.sqrt(n * sum_x_cua - (sum_x ** 2))) * (math.sqrt(n * sum_y_cua - (sum_y ** 2))))

        return r