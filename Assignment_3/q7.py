import numpy as np
def shiftedInverseIteration(A,shift):
    A = np.array([[6,2,1],[2,3,1],[1,1,1]])
    k =0
    x = np.array([0,0,1])
    smallestEigen = 0
    while(k<10000):
        y = np.linalg.solve(A-np.identity(3)*shift,x)
        x = y/np.linalg.norm(y,np.inf)
        smallestEigen = np.linalg.norm(y,np.inf)
        k = k+1
    smallestEigen = 1/smallestEigen + shift
    return x,smallestEigen

def eigenNumpy(A):
    return np.linalg.eig(A)

A = np.array([[6,2,1],[2,3,1],[1,1,1]])

shiftedInverseIterationRes = shiftedInverseIteration(A,2)
print("Shifted Inverse Iteration :")
print("The found eigenvalue is ",
      shiftedInverseIterationRes[1])
print("The corresponding eigenvector is ", shiftedInverseIterationRes[0])

numpyRes = eigenNumpy(A)
print("Numpy eigenvalues and eigenvectors :")
print("The eigenvalues are ", numpyRes[0])
print("The corresponding eigenvector columns are \n", numpyRes[1])
    