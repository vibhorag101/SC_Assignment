import numpy as np
import matplotlib.pyplot as plt


def fitData(alpha, beta):
    curveFit = np.exp(alpha*t+beta)/(1+np.exp(alpha*t+beta))
    return curveFit


t, y = np.loadtxt("Q5/data.txt", unpack=True)
plt.plot(t, y, 'o', label="Data", color='blue')
logY = np.log(y)
logYs = np.log(-1*y+1)

solY = logY - logYs

A = np.vstack([np.ones(len(t)), t]).T
AtA = np.matmul(A.T, A)
Atb = np.matmul(A.T, solY)
x = np.linalg.solve(AtA, Atb)
lineNP = x[1]*t+x[0]
xNPLS = np.linalg.lstsq(A, solY, rcond=None)[0]

lineNPLS = xNPLS[1]*t+xNPLS[0]

errorNP = np.linalg.norm(Atb - np.matmul(AtA, x))
errorNPLS = np.linalg.norm(solY - np.matmul(A, xNPLS))

print("Error using np.linalg.solve: ", errorNP)
print("Error using np.linalg.lstsq: ", errorNPLS)

plt.plot(t, fitData(x[1], x[0]),
         label='fit using np.linalg.solve', color='red')
plt.plot(t, fitData(xNPLS[1], xNPLS[0]),
         label='fit using np.linalg.lstsq', color='green', linestyle='--')
plt.legend()
plt.show()
