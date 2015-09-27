# -*- coding:utf-8 -*-

import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib import pyplot as plt

# Funcion Cuadratica
xi= []
xi_sig= []
fx= []

x_act= 0

print "{0:2s} | {1:10s} | {2:10s}".format("i","Xi","Xi+1")

for i in range(0,11):
    x_sig= (3 + x_act**2)/2.0

    xi.append(x_act)
    xi_sig.append(x_sig)

    print "{0:2d} | {1:10.2e} | {2:10.2e}".format(i, x_act, x_sig)

    fx.append(i**2 -2*i +3)
    x_act= x_sig

plt.plot(fx)
plt.show()

del xi
del x_sig
del fx