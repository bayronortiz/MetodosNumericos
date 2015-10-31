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
import matplotlib
#matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt
from matplotlib import gridspec

# Listas Globales
dafA= []        # Guarda los valores derivada hacia adelante funcion A
dafB= []        # Guarda los valores derivada hacia adelante funcion B
dafC= []        # Guarda los valores derivada hacia adelante funcion C

datfA= []         # Guarda los valores derivada hacia atrás funcion A
datfB= []        # Guarda los valores derivada hacia atrás funcion B
datfC= []        # Guarda los valores derivada hacia atrás funcion C

dcfA= []        # Guarda los valores derivada centrada funcion A
dcfB= []        # Guarda los valores derivada centrada funcion B
dcfC= []        # Guarda los valores derivada centrada funcion C

drfA= []        # Guarda los valores derivada real funcion A
drfB= []        # Guarda los valores derivada real funcion B
drfC= []        # Guarda los valores derivada real funcion C

# Se definen cada una de las funciones, recibe por parametro x:un valor para calcular la funcion
def funcionA(x):
    return math.exp(x) - 1

def funcionB(x):
    return math.sin(2*x)**3 + x**2

def funcionC(x):
    return x**4 + 3*x**2 - math.cos(x)

# Primera Derivada Real
def derivadaA(x):
    return math.exp(x)

def derivadaB(x):
    return 4*x**3 + 6*x + math.sin(x)

def derivadaC(x):
    return 6*(math.sin(2*x)**2) * math.cos(2*x) + 2*x

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

    derivadas=[]        # Guarda los valores de las derivadas hacia atras de cada funcion

    derivadas.append((funcionA(x_act)-funcionA(x_ant))/h)    # Calcula la derivada hacia atras de la funcion A
    derivadas.append((funcionB(x_act)-funcionB(x_ant))/h)    # Calcula la derivada hacia atras de la funcion B
    derivadas.append((funcionC(x_act)-funcionC(x_ant))/h)    # Calcula la derivada hacia atras de la funcion C

    return derivadas    # Devuelve la lista de los resultados


def derivadaCentrada(x,h):
    x_ant= x - h   # X anterior
    x_sig= x + h    # X siguiente o xi+1

    derivadas= []        # Guarda los valores de las derivadas centradas de cada funcion

    derivadas.append((funcionA(x_sig)-funcionA(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion A
    derivadas.append((funcionB(x_sig)-funcionB(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion B
    derivadas.append((funcionC(x_sig)-funcionC(x_ant))/(2*h))       # Calcula la derivada centrada de la funcion C

    return derivadas    # Devuelve la lista de los resultados


# Método calcular realiza la operación de calcular c/u de las derivadas de todas las funciones
# Param  h:Valor de Paso
def calcular(h):
    temp= []  # Lista temporal

    x= -5     # Inicializamos el valor de x, el intervalo va desde -5 a 5

    while x <= 5:
        temp= derivadaAdelante(x,h)       # Calcula Derivada hacia adelante

        dafA.append(temp[0])
        dafB.append(temp[1])
        dafC.append(temp[2])

        del temp[:]    # Limpiamos lista temporal

        temp= derivadaAtras(x,h)        # Calcula Derivada hacia atras

        datfA.append(temp[0])
        datfB.append(temp[1])
        datfC.append(temp[2])

        del temp[:]    # Limpiamos lista temporal

        temp= derivadaCentrada(x,h)        # Calcula Derivada centrada
        dcfA.append(temp[0])
        dcfB.append(temp[1])
        dcfC.append(temp[2])

        del temp[:]    # Limpiamos lista temporal

        drfA.append(derivadaA(x))    #Calcula derivada real y guarda en lista funcion A
        drfB.append(derivadaB(x))    #Calcula derivada real y guarda en lista funcion B
        drfC.append(derivadaC(x))    #Calcula derivada real y guarda en lista funcion C

        x+= h    #Incrementa el paso

# Imprime tabla de valores
# Param:  datos: lista con valores aprox  // datosR:lista derivadas reales   //
#          h: valor de paso  // etiqueta: tupla texto titulo tabla y texto funciones
def imprimirTabla(datosA, datosR, h, etiqueta):
    print "\n:::::: %s ::::::" % (etiqueta[0])
    print "f(x)= ",etiqueta[1]
    print "f\'(x)= ", etiqueta[2]
    print "\n{0:12s} | {1:12s} | {2:12s} | {3:12s} | {4:12s} | {5:12s} | {6:12s}".format("Valor X","f\'(x) Aprox", "f\'(x) Real", "Et", "|Et|","Er","Erp",)

    x= -5
    i= 0    #Contador de ciclo
    v_real= 0  # Valor real de la función derivada
    Et= 0   # Error Verdadero
    Eta= 0     # Error Verdadero Absoluto
    Er= 0    # Error Relativo
    Erp= 0   # Error Relativo Porcentual

    while x <= 5:
        v_real= datosR[i]
        Et= v_real - datosA[i]
        Eta= abs(Et)

        if v_real == 0:
            v_real= 1*10**-9

        Er= ((v_real - datosA[i])) / v_real
        Erp= Er*100

        print "{0:12f} | {1:12f} | {2:12f} | {3:12f} | {4:12f} | {5:12.2f} | {6:12.2f}".format(x,datosA[i], v_real, Et, Eta, Er , Erp)

        i+= 1
        x+= h


# Funcion graficar, realiza c/u de las graficas derivadas aproximadas y reales
def graficarDerivadas(h):
    valoresX= []
    x=-5

    while x <= 5:
        valoresX.append(x)
        x+= h

    fig= plt.figure("Graficas Derivadas")
    gs= gridspec.GridSpec(3, 1)    #Creamos la cuadricula 3 filas x 1 Columna

    gf1= fig.add_subplot(gs[0,0])
    plt.title("Funcion e^x - 1")
    dat,= gf1.plot(valoresX,datfA, "b-", label="Deriv. Atras")
    dc,= gf1.plot(valoresX,dcfA, "r-", label="Deriv. Centrada")
    da,= gf1.plot(valoresX,dafA, "g-", label="Deriv. Adelante")
    dr,= gf1.plot(valoresX,drfA, "k-", label="Deriv. Real")
    gf1.legend(handles= [dat,dc,da,dr], loc=2)
    gf1.grid(True)

    gf2= fig.add_subplot(gs[1,0])
    plt.title("Funcion sen(2x)^3  + x^2")
    gf2.plot(valoresX,datfB, "b-")
    gf2.plot(valoresX,dcfB, "r-")
    gf2.plot(valoresX,dafB, "g-")
    gf2.plot(valoresX,drfB, "k-")
    gf2.grid(True)

    gf3= fig.add_subplot(gs[2,0])
    plt.title("Funcion x^4 + 3x^2 - cos(x)")
    gf3.plot(valoresX,datfC, "b-")
    gf3.plot(valoresX,dcfC, "r-")
    gf3.plot(valoresX,dafC, "g-")
    gf3.plot(valoresX,drfC, "k-")
    gf3.grid(True)

    plt.show()

# -------------------------- Programa ------------------------------------------

h= input("\nIngrese Valor de Paso h--> ")

funciones=('e^x - 1', 'sen(2x)^3 + x^2', 'x^4 + 3x^2 - cos(x)')

calcular(h)

print "\nFUNCION e^x -1"
imprimirTabla(datfA, drfA, h, ("DERIVADA HACIA ATRAS","e^x - 1","e^x"))
imprimirTabla(dcfA,drfA, h, ("DERIVADA CENTRADA","e^x - 1","e^x"))
imprimirTabla(dafA,drfA, h, ("DERIVADA HACIA ADELANTE","e^x - 1","e^x"))

print "\n\n\nFUNCION sen(2x)^3  + x^2"
imprimirTabla(datfB,drfB, h, ("DERIVADA HACIA ATRAS","sen(2x)^3  + x^2","6*Sen(2x)^2 * Cos(2x) + 2x"))
imprimirTabla(dcfB,drfB, h, ("DERIVADA CENTRADA","sen(2x)^3  + x^2","6*Sen(2x)^2 * Cos(2x) + 2x"))
imprimirTabla(dafB,drfB, h, ("DERIVADA HACIA ADELANTE","sen(2x)^3  + x^2","6*Sen(2x)^2 * Cos(2x) + 2x"))

print "\n\n\nFUNCION x^4 + 3x^2 - cos(x)"
imprimirTabla(datfC,drfC, h, ("DERIVADA HACIA ATRAS", "sen(2x)^3  + x^2", "4x^3 + 6x + sen(x)"))
imprimirTabla(dcfC,drfC, h, ("DERIVADA CENTRADA", "sen(2x)^3  + x^2", "4x^3 + 6x + sen(x)"))
imprimirTabla(dafC,drfC, h, ("DERIVADA HACIA ADELANTE", "sen(2x)^3  + x^2", "4x^3 + 6x + sen(x)"))


# Muestra graficas
graficarDerivadas(h)
