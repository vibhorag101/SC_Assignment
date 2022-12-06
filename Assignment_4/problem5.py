import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate
hvalues = []
for i in range(1,16):
    hvalues.append(10**(-i))
relativeError = []

def exactDifferential(x):
    cosTerm = math.cos(x**3)
    sinTerm = -math.sin(x**3)/4
    expTerm = math.exp(sinTerm)
    diff = (-0.75)*(x**2)*cosTerm*expTerm
    return diff

def function(x):
    return math.exp(-math.sin(x**3)/4)

def forwardDifferential(x, h):
    return((function(x+h) - function(x))/h)

for h in hvalues:
    relativeError.append(math.log10(abs((forwardDifferential(1, h) - exactDifferential(1))/exactDifferential(1))))

hvalues = [ math.log10(h) for h in hvalues ]
table = []
for i in range(len(hvalues)):
    table.append([hvalues[i], relativeError[i]])
print(tabulate(table, headers=['log(h)', 'log(relative error)'], tablefmt= 'fancy_grid'))
plt.plot(hvalues, relativeError)
plt.xlabel('h')
plt.ylabel('Relative Error')
plt.title('log Relative Error vs. log h')
plt.show()

