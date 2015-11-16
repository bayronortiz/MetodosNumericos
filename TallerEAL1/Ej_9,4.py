#-*-coding:utf-8 -*-

'''
	Descripción: Ejercicio 9.4, Usando el método gráfico para resolver el sistema ecuaciones dado.
	Elaborado:	 Bayron Danilo Ortiz Foronda - 160002925
	Curso:		 Métodos Numéricos - 2015
	Versión:	 Python2.7
'''

from matplotlib import pyplot as plt


# Definimos la funcion1 original 4X1 - 8X2 = -24
def f1(x1, x2):
	return 4 * x1 - 8 * x2

# Definimos la funcion2 original X1 + 6X2 = 174
def f2(x1, x2):
	return x1 + 6 * x2

# Define la función 4X1 - 8X2 = -24 despejando X2
# X2 = (-24 - 4X1) / -8
def f1_d(x1):
	return (-24 - 4 * x1) / -8.0

# Define la función X1 + 6X2 = 174 despejando X2
# X2 = (174 - X1) / 6
def f2_d(x1):
	return (174 - x1) / 6.0


#Inicio del Programa
print "Sistema Ecuaciones Dado: "
print "4X1 - 8X2 = -24\nX1 + 6X2 = 174"

# Usando método gráfico, tenemos lo siguiente
val_f1 = []
val_f2 = []
x = []

#Asignamos los valores
for i in range(0,50):
	x.append(i)
	val_f1.append(f1_d(i))
	val_f2.append(f2_d(i))

#Encuentra los valores donde se interceptan las gráficas
for i in range(0,50):
	if val_f1[i] == val_f2[i]:
		x1, x2 = (x[i], val_f2[i])
		break

print "\nLas Soluciones son: "
print "X1= ", x1, "\tX2= ", x2
print "\nSustituyendo Valores Tenemos:"
print "4(%.1f) - 8(%.1f) = %.1f" % (x1, x2, f1(x1,x2))
print "%.1f + 6(%.1f) = %.1f" % (x1, x2, f2(x1, x2))

# Graficamos los dos sistemas
plt.figure(u"Solución Gráfica Ej_9,4")
plt.title(u"Solución Gráfica")
gf1, = plt.plot(x, val_f1, label= "4X1 - 8X2 = -24")
gf2, = plt.plot(x, val_f2, label= "X1 + 6X2 = 174")
plt.legend(handles=[gf1, gf2], loc= 4)
plt.grid(True)
plt.show()

