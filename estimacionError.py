# Fecha: 24-Ago-2015

# Calcula el error de la funcion exponencial usando series de maclaurin

from math import *

x= input("Ingrese Valor de (X)--> ")
n= input("Ingrese Cifras Significativas (n)--> ")

Es= 0.5*10**(2-n)  # Error tolerado/aceptable

valor_aprox_act= 1
valor_aprox_ant= 0
Ea= 0
it= 1

print "\nError Tolerado: ",Es,"%"
print "\nIter | Valor Actual | Valor Anterior | Ea\n"

Ea= (valor_aprox_act - valor_aprox_ant)/valor_aprox_act

while True:
    print "%d | %f | %f | %f\n" %(it, valor_aprox_act, valor_aprox_ant, Ea)

    valor_aprox_ant= valor_aprox_act
    valor_aprox_act= ((x**it)/factorial(it)) + valor_aprox_ant
    Ea= (valor_aprox_act - valor_aprox_ant)/valor_aprox_act    
    it+=1 
    
    if Ea < Es:
        print "%d | %f | %f | %f\n" %(it, valor_aprox_act, valor_aprox_ant, Ea)
        break
   
   


