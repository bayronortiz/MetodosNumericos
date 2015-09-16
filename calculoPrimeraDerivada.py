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

        x+= h    #Incrementa el paso

# Imprime tabla de valores
# Param:  datos: lista con valores aprox  // h: valor de paso  // titulo: texto titulo tabla
def imprimirTabla(datos, h, titulo):
    print "\n:::::: %s ::::::" % (titulo)
    print "{0:10s} | {1:10s} | {2:10s} | {3:10s} | {4:10s} | {5:10s} | {6:10s}".format("Valor X", "e^x - 1", "e^x", "E", "|Et|","Er","Erp",)

    x= -5
    i= 0    #Contador de ciclo
    v_real= 0  # Valor real de la función derivada
    Et= 0   # Error Verdadero
    Eta= 0     # Error Verdadero Absoluto
    Er= 0    # Error Relativo
    Erp= 0   # Error Relativo Porcentual

    while x <= 5:
        v_real= derivadaA(x)    # Calcula el valor en la derivada real de la función
        Et= v_real - datos[i]
        Eta= abs(Et)
        Er= (abs(v_real - datos[i])) / v_real
        Erp= Er * 100

        print "{0:10f} | {1:10f} | {2:10f} | {3:10f} | {4:10f} | {5:10f} | {6:10.2f}".format(x,datos[i], v_real, Et, Eta, Er , Erp)

        i+= 1
        x+= h
# -------------------------- Programa ------------------------------------------

h= input("Ingrese Valor de Paso h--> ")

funciones=('e^x - 1', 'sen(2x)^3 + x^2', 'x^4 + 3x^2 - cos(x)')

calcular(h)

#imprimirTablaA(dafA, datfA, dcfA, h)
imprimirTabla(dafA, h, "DERIVADA HACIA ADELANTE")
imprimirTabla(datfA, h, "DERIVADA HACIA ATRAS")
imprimirTabla(dcfA, h, "DERIVADA CENTRADA")