import numpy as np
def shiftedInverseIteration():
    A = np.array([[6,2,1],[2,3,1],[1,1,1]])
    k =0
    x = np.array([0,0,1])
    smallestEigen = 0
    while(k<10000):
        y = np.linalg.solve(A-np.identity(3)*2,x)
        x = y/np.linalg.norm(y,np.inf)
        smallestEigen = np.linalg.norm(y,np.inf)
        k = k+1
    smallestEigen = 1/smallestEigen + 2
    return smallestEigen,x

def eigenNumpy():
    A = np.array([[6,2,1],[2,3,1],[1,1,1]])
    return np.linalg.eig(A)

print(shiftedInverseIteration())
print(eigenNumpy())

    