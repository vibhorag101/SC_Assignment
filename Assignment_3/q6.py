import numpy as np
def normalisedPowerIteration():
    A = np.array([[2,3,2],[10,3,4],[3,6,1]])
    k =0
    x = np.array([0,0,1])
    while(k<10000):
        y = np.matmul(A,x)
        x = y/np.linalg.norm(y,np.inf)
        k = k+1
    return x

def inversePowerIteration():
    A = np.array([[2,3,2],[10,3,4],[3,6,1]])
    k =0
    x = np.array([0,0,1])
    while(k<100000):
        y = np.linalg.solve(A,x)
        x = y/np.linalg.norm(y,np.inf)
        k = k+1
    return x

def eigenNumpy():
    A = np.array([[2,3,2],[10,3,4],[3,6,1]])
    return np.linalg.eig(A)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(normalisedPowerIteration())
print(inversePowerIteration())
print(eigenNumpy())

