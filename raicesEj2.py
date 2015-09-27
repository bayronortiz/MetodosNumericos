# -*-coding: utf-8 -*-

import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt
import math

fx= []

for x in range(0,11):
    valorFx= math.exp(-x) - x
    fx.append( valorFx)

    if valorFx == 0:
        print "Cruce en Cero: ", x

plt.plot(fx)
plt.grid(True)
plt.show()