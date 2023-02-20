import numpy as np
import matplotlib.pyplot as plt
import random
x_noisy = np.loadtxt("Q7/denoising.txt")
def plotSignal(x,lam,col):
    plt.plot(np.arange(1, 1 + len(x)), x,
    color=col, label="lambda = {}".format(lam))
    plt.legend(loc='upper right')

color = ['blue', 'red', 'green', 'yellow']
def denoising(lam,col):
    D = np.zeros((999, 1000))
    for i in range(999):
        D[i,i]=-1
        D[i,i+1]=1
    A = np.identity(1000) + lam * np.matmul(D.T, D)
    b = x_noisy
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    # x= np.linalg.solve(A, b)
    plotSignal(x, lam,color[col])

plt.figure()
plt.xlabel("$n$", fontsize=14)
plt.ylabel("$x_{noisy}$", fontsize=14)
plt.gcf().tight_layout()
plotSignal(x_noisy, 0,color[0])
denoising(1,1)
denoising(100,2)
denoising(10000,3)
plt.show()