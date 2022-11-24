import numpy as np


def normalisedPowerIteration(A):
    largestEigen = 0
    k = 0
    x = np.array([0, 0, 1])
    while(k < 10000):
        y = np.matmul(A, x)
        x = y/np.linalg.norm(y, np.inf)
        k = k+1
        largestEigen = np.linalg.norm(y, np.inf)
    return x, largestEigen


def inversePowerIteration(A):
    smallestEigen = 0
    k = 0
    x = np.array([0, 0, 1])
    while(k < 10000):
        y = np.linalg.solve(A, x)
        x = y/np.linalg.norm(y, np.inf)
        k = k+1
        smallestEigen = 1/np.linalg.norm(y, np.inf)
    return x, smallestEigen


def eigenNumpy(A):
    return np.linalg.eig(A)


A = np.array([[2, 3, 2], [10, 3, 4], [3, 6, 1]])

normalisedPowerIterationRes = normalisedPowerIteration(A)
print("Normalised Power Iteration :")
print("The found largest magnitude eigenvalue is ",
      normalisedPowerIterationRes[1])
print("The corresponding eigenvector is ", normalisedPowerIterationRes[0])

inversePowerIterationRes = inversePowerIteration(A)
print("Inverse Power Iteration :")
print("The found smallest magnitude eigenvalue is ",
      inversePowerIterationRes[1])
print("The corresponding eigenvector is ", inversePowerIterationRes[0])

numpyRes = eigenNumpy(A)
print("Numpy eigenvalues and eigenvectors :")
print("The eigenvalues are ", numpyRes[0])
print("The corresponding eigenvector columns are \n", numpyRes[1])
