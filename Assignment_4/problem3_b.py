import numpy as np
import matplotlib.pyplot as plt
import math
def runge(x):
    return 1/(1+25*x**2)

def cubicSplineInterpolate(xPoint,yPoint,n):
    x = np.zeros(4*n-4)
    A= np.zeros((4*n-4,4*n-4))
    b = np.zeros(4*n-4)
    for i in range(n):
        b[i] = yPoint[i]

    for i in range(n-1):
        start = 4*i
        A[i,start] = 1
        A[i,start+1] = xPoint[i]
        A[i,start+2] = xPoint[i]**2
        A[i,start+3] = xPoint[i]**3
    A[n-1,4*n-8] = 1
    A[n-1,4*n-7] = xPoint[n-1]
    A[n-1,4*n-6] = xPoint[n-1]**2
    A[n-1,4*n-5] = xPoint[n-1]**3


    for i in range(0,n-2):
        start = 4*i
        A[i+n,start] = 1
        A[i+n,start+1] = xPoint[i+1]
        A[i+n,start+2] = xPoint[i+1]**2
        A[i+n,start+3] = xPoint[i+1]**3
        A[i+n,start+4] = -1
        A[i+n,start+5] = -xPoint[i+1]
        A[i+n,start+6] = -xPoint[i+1]**2
        A[i+n,start+7] = -xPoint[i+1]**3

    for i in range(0,n-2):
        start = 4*i
        A[i+2*n-2,start+1] = 1
        A[i+2*n-2,start+2] = 2*xPoint[i+1]
        A[i+2*n-2,start+3] = 3*xPoint[i+1]**2
        A[i+2*n-2,start+5] = -1
        A[i+2*n-2,start+6] = -2*xPoint[i+1]
        A[i+2*n-2,start+7] = -3*xPoint[i+1]**2

    for i in range(0,n-2):
        start = 4*i
        A[i+3*n-4,start+2] = 2
        A[i+3*n-4,start+3] = 6*xPoint[i+1]
        A[i+3*n-4,start+6] = -2
        A[i+3*n-4,start+7] = -6*xPoint[i+1]
    
    A[4*n-6,1] = 1
    A[4*n-6,2] = 2*xPoint[0]
    A[4*n-6,3] = 3*xPoint[0]**2
    A[4*n-5,4*n-7] = 1
    A[4*n-5,4*n-6] = 2*xPoint[n-2]
    A[4*n-5,4*n-5] = 3*xPoint[n-2]**2
    x = np.linalg.solve(A,b)
    return x

def evaluateCubic(x,c,xPoint,n):
    ans = []
    for pt in x:
        sum = 0
        for i in range(n-1):
            if xPoint[i] <= pt and xPoint[i+1] >= pt:
                start = 4*i
                sum += c[start] + c[start+1]*pt + c[start+2]*pt**2 + c[start+3]*pt**3
                ans.append(sum)
                break
    return ans



if __name__=='__main__':
    x = np.linspace(-1,1,1000)
    y = [ runge(x) for x in x ]
    x11 = np.linspace(-1,1,11)
    y11 = [ runge(x) for x in x11 ]
    c11 = cubicSplineInterpolate(x11,y11,11)
    print(c11)
    x21 = np.linspace(-1,1,21)
    y21 = [ runge(x) for x in x21 ]
    c21 = cubicSplineInterpolate(x21,y21,21)
    yInterp11 = evaluateCubic(x,c11,x11,11)
    yInterp21 = evaluateCubic(x,c21,x21,21)
    plt.title('Runge Function Polynomial Interpolation n=11')
    plt.plot(x,y,label='Runge Function, n=11',color='red')
    plt.plot(x,yInterp11,label='Interpolated Runge Function , n=11',color='blue',linestyle='dashed')
    plt.show()
    plt.title('Runge Function Polynomial Interpolation n=21')
    plt.plot(x,y,label='Runge Function, n=21',color='green')
    plt.plot(x,yInterp21,label='Interpolated Runge Function , n=21',color='blue',linestyle='--')
    plt.show()



