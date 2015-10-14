# -*-coding:utf-8 -*-

'''
    Expansión Series de Taylor f(x)= 3Cos(2x)
    Elaborado Bayron Danilo Ortiz Foronda    Cod 160002925
'''
import math

def orden0(x):
    return 3*math.cos(2*x)

def orden1(x,h):
    return orden0(x) + (-6*math.sin(2*x)) * h

def orden2(x,h):
    return orden1(x,h) + ((-12 * math.cos(2*x)) / math.factorial(2)) * h**2

def orden3(x,h):
    return orden2(x,h) + ((24 * math.sin(2*x)) / math.factorial(3)) * h**3

def orden4(x,h):
    return orden3(x,h) + ((48 * math.cos(2*x)) / math.factorial(4)) * h**4

def orden5(x,h):
    return orden4(x,h) + ((-96 * math.sin(2*x)) / math.factorial(5)) * h**5

serieTaylor = 0
Et = 0
aprox_act = 0
aprox_ant = 0

h = math.pi / 12.0
xii = math.pi / 4.0    # Xi+1
xi = xii - h

print "{0:3s} | {1:10s} | {2:10s}".format("Ord", "Serie", "Et%")

for i in range(6):
    if i == 0:
        serieTaylor = orden0(xi)

    if i == 1:
        serieTaylor = orden1(xi,h)

    if i == 2:
        serieTaylor = orden2(xi,h)

    if i == 3:
        serieTaylor = orden3(xi,h)

    if i == 4:
        serieTaylor = orden4(xi,h)

    if i == 5:
        serieTaylor = orden5(xi,h)

    aprox_ant = aprox_act
    aprox_act = serieTaylor

    Et = abs(((aprox_act - aprox_ant) / aprox_act)) * 100

    print "{0:3d} | {1:10f} | {2:10f}".format(i, serieTaylor, Et)