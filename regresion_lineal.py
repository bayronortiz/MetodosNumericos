#-*-coding:utf-8 -*-
'''
    Descripción: Script genera gráfica de dispersión de los datos (edad estudiantes) y
                 calcula la linea de regresión.

	Elaborado:	 Bayron Danilo Ortiz Foronda.

	Version Python: 2.7
'''

import matplotlib.pyplot as plt

# Función que calcula la sumatoria de una serie de datos
# param: v_val:vector
# return: sum:numerico
def sumatoria(v_val):
    sum = 0     #Guarda el valor de la sumatoria

    for i in v_val:     #Sumamos c/u de los valores
        sum += i

    return sum      #Retornamos la suma


# Función calcula la media de los datos
# param: v_val:vector
# return: media:numeric
def calc_media(v_val):
    return sumatoria(v_val) / float(len(v_val))   # Devuelve la media de los datos


# Función que calcula el coeficiente a1
# param: v_x:vector, v_y:vector, v_xy:vector
# return: a1:numeric
def calc_a1(v_x, v_y, v_xy, v_x_cuad):
    n = len(v_x)    # Tamanio
    sum_xy = sumatoria(v_xy)    #sumatoria xi*yi
    sum_x = sumatoria(v_x)      #sumatoria valores de x (consecutivo)
    sum_y = sumatoria(v_y)      #sumatoria valores de y (datos)
    sum_x_cua = sumatoria(v_x_cuad)     #sumatoria de xi²
    
    a1 = ((n * sum_xy) - (sum_x * sum_y)) / float(((n * sum_x_cua) - (sum_x**2)))
    
    return a1

# Función que calcula el coeficiente a0
# param: v_x:vector, v_y:vector, a1:float
# return a0:numeric
def calc_a0(v_x, v_y, a1):
    x_med = calc_media(v_x)
    y_med = calc_media(v_y)

    print x_med
    print y_med
    return float(y_med - a1 * x_med)


#Inicio del Programa
edades = [19, 19, 23, 21, 21, 21, 19, 18, 20, 22, 22, 21, 19, 19, 20, 20, 20, 21, 20, 23]
x = []      #Vector "x" equivale al consecutivo
y = []      #Vector "y" equivale a los datos edades
xy = []     #Vector "xy" guarda el producto consecutivo x edades
x_cuad = []     #Vector "x²" guarda consecutivo al cuadrado
a0 = 0      #Coeficientes de la recta de regresión
a1 = 0      #Coeficinetes de la recta de regresión
recta = []  #Lista guarda valores de la recta

for xi, yi in enumerate(edades, start=1):
    x.append(xi)
    y.append(yi)
    xy.append(xi * yi)
    x_cuad.append(xi**2)

a1 = calc_a1(x, y, xy, x_cuad)      #Hallamos coeficiente a1
a0 = calc_a0(x, y, a1)          #Hallamos coeficinete a0

for i in x:     #Calculamos los valores para y en la recta de regresión
    recta.append(float(a0 + a1*i))


print "\nGRAFICO DISPERSION Y RECTA REGRESIÓN"
print "\nEdades: "
print "\t", edades
print "\nCoeficientes Recta: "
print "\ta0= ", a0, "\ta1= ", a1
print "\nEcuación de la Recta: "
print "\ty= %.2f + %.2f * x\n" % (a0, a1)

# Graficamos modelo dispersion y la recta de regresión
plt.figure(u"Gráfica Regresión")
plt.title(u"Regresión Lineal", fontweight="bold")
plt.plot(x, y, "ro", label= "Edad Estudiantes")        #Valores dispersion
plt.plot(x, recta, label=u"Recta Regresión", lw=1.5)          #Recta de regresión
plt.legend(loc=4)
plt.margins(y=.1, x=.1)
plt.grid(True)
plt.show()
