import numpy as np
import matplotlib.pyplot as plt
import math
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

def forwardDifferential(x, h):
    return((exactDifferential(x+h) - exactDifferential(x))/h)

for h in hvalues:
    relativeError.append(math.log10(abs((forwardDifferential(1, h) - exactDifferential(1))/exactDifferential(1))))

hvalues = [ math.log10(h) for h in hvalues ]
plt.plot(hvalues, relativeError)
plt.xlabel('h')
plt.ylabel('Relative Error')
plt.title('log Relative Error vs. log h')
plt.show()

