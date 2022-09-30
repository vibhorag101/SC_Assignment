import numpy as np
from tabulate import tabulate

def gaussianElimination(A, b):
    n = np.shape(A)[0]
    for k in range(1, n):
        for i in range(k+1, n+1):
            atemp = A[i-1, k-1]/A[k-1, k-1]
            A[i-1, k-1] = atemp
            for j in range(k+1, n+1):
                A[i-1, j-1] = A[i-1, j-1] - atemp*A[k-1, j-1]
            b[i-1] = b[i-1] - atemp*b[k-1]

    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1, n-1]

    for i in range(n-1, 0, -1):
        sum = b[i-1]
        for j in range(i+1, n+1):
            sum = sum - A[i-1, j-1]*x[j-1]
        x[i-1] = sum/A[i-1, i-1]
    return x

def gaussianEliminationPartial(A, b):
    n = np.shape(A)[0]
    l = [0]*n
    s = [0] * n
    for i in range(1, n+1):
        l[i-1] = i
        smax = 0
        for j in range(1, n+1):
            smax = max(smax, abs(A[i-1, j-1]))
        s[i-1] = smax

    for k in range(1, n):
        rmax = 0
        # j=0
        for i in range(k, n+1):
            r = abs(A[l[i-1]-1, k-1]/s[l[i-1]-1])
            if r > rmax:
                rmax = r
                j = i

        ltemp = l[k-1]
        l[k-1] = l[j-1]
        l[j-1] = ltemp

        for i in range(k+1, n+1):
            amult = A[l[i-1]-1, k-1]/A[l[k-1]-1, k-1]
            A[l[i-1]-1, k-1] = amult
            for j in range(k+1, n+1):
                A[l[i-1]-1, j-1] = A[l[i-1]-1, j-1] - amult*A[l[k-1]-1, j-1]

    for k in range(1, n):
        for i in range(k+1, n+1):
            b[l[i-1]-1] = b[l[i-1]-1] - A[l[i-1]-1, k-1]*b[l[k-1]-1]
    x = [0]*n
    x[n-1] = b[l[n-1]-1]/A[l[n-1]-1, n-1]
    for i in range(n-1, 0, -1):
        sum = b[l[i-1]-1]
        for j in range(i+1, n+1):
            sum = sum - A[l[i-1]-1, j-1]*x[j-1]
        x[i-1] = sum/A[l[i-1]-1, i-1]
    return x


def makeRandom(n):
    return np.random.random_sample((n, n))

def makeHilbert(n):
    return (np.fromfunction(lambda i, j: 1/(i+j+1), (n, n)))

def makeX(n):
    return np.ones(n)

def makeOneMatrix(n):
    A = np.zeros((n, n))
    for i in range(0, n):
        for j in range(0,n):
            if (j<i):
                A[i,j] = -1
            else:
                A[i,j] = 1
    return A

def makeB(A):
    n = np.shape(A)[0]
    x = np.ones(n)
    return(np.matmul(A, x))

def matrixMaker(j,i):
    if (j == 0):
        return makeRandom(i)
    elif (j == 1):
        return makeHilbert(i)
    elif (j == 2):
        return makeOneMatrix(i)
def matrixName(j):
    if (j == 0):
        return "Random"
    elif (j == 1):
        return "Hilbert"
    elif (j == 2):
        return "One Matrix"

if __name__ == "__main__":
    print("GE is Gaussian Elimination, GPE is Gaussian Elimination with Partial Pivoting, N is numpy.linalg.solve")
    print("")
    for i in range (10,41,10):
        dataList = [[]]
        for j in range(3):
            A = matrixMaker(j,i)
            b = makeB(A)
            x = makeX(i)
            normX = np.linalg.norm(x)
            normA = np.linalg.norm(A)
            xGE= gaussianElimination(A.copy(), b.copy())
            xGPE = gaussianEliminationPartial(A.copy(), b.copy())
            xN = np.linalg.solve(A.copy(), b.copy())
            conditionNumber = np.linalg.cond(A)
            errorGE = np.linalg.norm(xGE-x)/normX
            errorGPE = np.linalg.norm(xGPE-x)/normX
            errorN = np.linalg.norm(xN-x)/normX
            residualGE = np.linalg.norm(np.matmul(A, xGE)-b)/(normA*normX)
            residualGPE = np.linalg.norm(np.matmul(A, xGPE)-b)/(normA*normX)
            residualN = np.linalg.norm(np.matmul(A, xN)-b)/(normA*normX)
            matrixType = matrixName(j)
            dataList.append([matrixType, conditionNumber, errorGE, errorGPE, errorN, residualGE, residualGPE, residualN])

        print("for n=", i)
        print(tabulate(dataList, headers=["Matrix", "Condition Number", "Error GE", "Error GPE", "Error Numpy", "Residual GE", "Residual GPE", "Residual Numpy"]))
        print("")
            






