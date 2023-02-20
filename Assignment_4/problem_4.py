import numpy as np
import matplotlib.pyplot as plt
import math
from tabulate import tabulate


def function(x):
    return((100/x)*math.sin(10/x))


def limitChangeX(a, b):
    x1 = 1/(3**0.5)
    x2 = -1*x1
    xChange1 = ((b-a)*x1 +a - (b*-1))/2
    xChange2 = ((b-a)*x2 +a - (b*-1))/2
    return(function(xChange1) + function(xChange2))*((b-a)/2)   

interpolatedValues = []
relativeError = []
nValues = [n for n in range(2, 65,2)]
for n in nValues:
    h = 2/n
    sum = 0
    temp = int(n/2)+1
    for i in range(1, temp):
        a = 1 + 2*(i-1)*h
        b = a + 2*h
        sum += limitChangeX(a, b)
    interpolatedValues.append(sum)
    relativeError.append(abs((sum+(18.79829683678703))/-18.79829683678703))

table = []
for i in range(len(nValues)):
    table.append([nValues[i], interpolatedValues[i], relativeError[i]])
print(tabulate(table, headers=['n', 'Interpolated Value', 'Relative Error'], tablefmt= 'fancy_grid'))

plt.plot(nValues, interpolatedValues)
plt.xlabel('n')
plt.ylabel('Interpolated Value')
plt.title('Interpolated Value vs. n')
plt.show()



