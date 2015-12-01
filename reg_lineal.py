#-*-coding:utf-8 -*-

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
            sum_cua += i**2

        return sum_cua


    # Función calcula la media de los datos
    # param: v_val:vector
    # return: media:numeric
    def calc_media(self,v_val):
        return self.sumatoria(v_val) / float(len(v_val))   # Devuelve la media de los datos


    # Función que calcula el coeficiente a1
    # param: v_x:vector, v_y:vector, v_xy:vector
    # return: a1:numeric
    def calc_a1(self,v_x, v_y, v_xy, v_x_cuad):
        n = len(v_x)    # Tamanio
        sum_xy = self.sumatoria(v_xy)    #sumatoria xi*yi
        sum_x = self.sumatoria(v_x)      #sumatoria valores de x (consecutivo)
        sum_y = self.sumatoria(v_y)      #sumatoria valores de y (datos)
        sum_x_cua = self.sumatoria(v_x_cuad)     #sumatoria de xi²

        a1 = ((n * sum_xy) - (sum_x * sum_y)) / float(((n * sum_x_cua) - (sum_x**2)))

        return a1

    # Función que calcula el coeficiente a0
    # param: v_x:vector, v_y:vector, a1:float
    # return a0:numeric
    def calc_a0(self,v_x, v_y, a1):
        x_med = self.calc_media(v_x)
        y_med = self.calc_media(v_y)

        #print x_med
        #print y_med
        return float(y_med - a1 * x_med)


