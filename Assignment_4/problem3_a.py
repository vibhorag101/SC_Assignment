import numpy as np
import matplotlib.pyplot as plt
import math
def runge(x):
    return 1/(1+25*x**2)

def polynomialInterpolate(x,y):
    n = len(x)
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            A[i,j] = x[i]**j
    b = np.zeros(n)
    for i in range(n):
        b[i] = y[i]
    c = np.linalg.solve(A,b)
    return c

def polynomialEval(c,x):
    n = len(c)
    y = 0
    for i in range(n):
        y += c[i]*x**i
    return y

if __name__=='__main__':
    x = np.linspace(-1,1,1000)
    y = [ runge(x) for x in x ]
    x11 = np.linspace(-1,1,11)
    y11 = [ runge(x) for x in x11 ]
    c11 = polynomialInterpolate(x11,y11)
    x21 = np.linspace(-1,1,21)
    y21 = [ runge(x) for x in x21 ]
    c21 = polynomialInterpolate(x21,y21)
    yInterp11 = [ polynomialEval(c11,x) for x in x ]
    yInterp21 = [ polynomialEval(c21,x) for x in x ]
    plt.title('Runge Function Polynomial Interpolation n=11')
    plt.plot(x,y,label='Runge Function, n=11',color='red')
    plt.plot(x,yInterp11,label='Interpolated Runge Function , n=11',color='blue',linestyle='dashed')
    plt.show()
    plt.title('Runge Function Polynomial Interpolation n=21')
    plt.plot(x,y,label='Runge Function, n=21',color='green')
    plt.plot(x,yInterp21,label='Interpolated Runge Function , n=21',color='blue',linestyle='--')
    plt.legend()
    plt.show()



