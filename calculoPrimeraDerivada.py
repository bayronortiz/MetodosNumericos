# -*- coding= utf-8 -*-
'''
    Este Archivo Calcula La Primera Derivada usando tres definiciones de varias funciones
    A)e^x - 1
    B)sen(2x)^3  + x^2
    C)x^4 + 3x^2 - cos x

    Elaborado: Bayron Danilo Ortiz Foronda

    Fecha: 14-Sept-2015
'''
import math

# Se definen cada una de las funciones, recibe por parametro x:un valor para calcular la funcion
def funcionA(x):
    return math.exp(x) - 1


def funcionB(x):
    return math.sin(2*x)**3 + x**2


def funcionC(x):
    return x**4 + 3*x**2 - math.cos(x)


# Se definen cada una de las derivadas, param x: valor arbitrario -- h:valor de paso
def derivadaAdelante(x,h):
    x_act= x    # X actual
    x_sig= x + h    # X siguiente o xi+1

    derivadas=[]        # Guarda los valores de las derivadas hacia adelante de cada funcion

    derivadas.append((funcionA(x_sig)-funcionA(x_act))/(x_sig - x_act))  # Calcula derivada hacia adelante funcion A
    derivadas.append((funcionB(x_sig)-funcionB(x_act))/(x_sig - x_act))  # Calcula derivada hacia adelante funcion B
    derivadas.append((funcionC(x_sig)-funcionC(x_act))/(x_sig - x_act))  # Calcula derivada hacia adelante funcion C

    return derivadas        # Devuelve la lista de los resultados


def derivadaAtras(x,h):
    x_act= x    # X actual
    x_ant= x - h   # X anterior

    derivadas=[]

    derivadas.append((funcionA(x_act)-funcionA(x_ant))/h)    # Calcula la derivada hacia atras de la funcion A
    derivadas.append((funcionB(x_act)-funcionB(x_ant))/h)    # Calcula la derivada hacia atras de la funcion B
    derivadas.append((funcionC(x_act)-funcionC(x_ant))/h)    # Calcula la derivada hacia atras de la funcion C

    return derivadas    # Devuelve la lista de los resultados


def derivadaCentrada(x,h):
    x_ant= x - h   # X anterior
    x_sig= x + h    # X siguiente o xi+1

    derivadas= []

    derivadas.append((funcionA(x_sig)-funcionA(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion A
    derivadas.append((funcionB(x_sig)-funcionB(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion B
    derivadas.append((funcionC(x_sig)-funcionC(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion C

    return derivadas    # Devuelve la lista de los resultados


x= input("\nIngrese Valor de X--> ")
h= input("Ingrese Valor de Paso h--> ")

funciones=('e^x - 1', 'sen(2x)^3  + x^2', 'x^4 + 3x^2 - cos x')
adelante= derivadaAdelante(x,h)
atras= derivadaAtras(x,h)
centro= derivadaCentrada(x,h)

print "\nValores X:\n x_act= %f -- x_sig= %f  -- x_ant= %f" % (x,x+h, x-h)

print "\n\nFuncion  |  Derivada Adel  |  Derivada Atras  |  Derivada Centro  \n"

for i in range(3):
    print "%s  |  %f  |  %f  |  %f  \n" % (funciones[i], adelante[i], atras[i], centro[i])

print "\n"