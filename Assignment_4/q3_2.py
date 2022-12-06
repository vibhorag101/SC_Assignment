# compute cubic spline interpolants to f(x) = 1/(1 + 25x^2) on [-1, 1] using n= 11,21 equispaced nodes
# and plot the interpolants and the function f(x) on [-1, 1] for n= 11,21

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1 + 25*x**2)

def cubic_spline(x, xj, yj):
    # x: array of points to evaluate the interpolant
    # xj: array of interpolation nodes
    # yj: array of function values at the interpolation nodes
    # returns: array of function values at the points x
    n = len(xj)
    y = np.zeros(len(x))
    for i in range(n-1):
        a = yj[i]
        b = (yj[i+1] - yj[i])/(xj[i+1] - xj[i])
        c = 0
        d = 0
        for j in range(i+1, n-1):
            c = c + (yj[j+1] - yj[j])/(xj[j+1] - xj[j])
        c = (c - b)/(xj[i+1] - xj[i])
        for j in range(i+1, n-1):
            d = d + (yj[j+1] - yj[j])/(xj[j+1] - xj[j]) - c
        d = (d - c)/(xj[i+1] - xj[i])
        idx = np.where((x >= xj[i]) & (x <= xj[i+1]))
        y[idx] = a + b*(x[idx] - xj[i]) + c*(x[idx] - xj[i])**2 + d*(x[idx] - xj[i])**3
    return y

def plot_interpolants(n):
        
        x = np.linspace(-1, 1, 1000)
        y = f(x)
        xj = np.linspace(-1, 1, n)
        yj = f(xj)
        yL = cubic_spline(x, xj, yj)
        plt.plot(x, y, label='f(x)')
        plt.plot(x, yL, label='cubic spline')
        plt.legend()
        plt.show()

plot_interpolants(11)
plot_interpolants(21)



