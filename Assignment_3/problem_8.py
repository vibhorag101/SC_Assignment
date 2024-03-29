import numpy as np
import math
def RayleighQuotientIteration(A,trueEigen):
    k =0
    e0,e1,e2 = 0,0,0
    x = np.random.rand(A.shape[0])
    smallestEigen = 0
    sigma = 0
    while(k<10000):
        sigma = np.matmul(np.transpose(x),np.matmul(A,x))/np.matmul(np.transpose(x),x)
        if(np.linalg.det(A-sigma*np.identity(3))==0):
            k+=1
            continue
        y = np.linalg.solve(A-sigma*np.identity(3),x)
        x = y/np.linalg.norm(y,np.inf)
        smallestEigen = np.linalg.norm(y,np.inf)
        smallestEigen = 1/smallestEigen + sigma
        if(k==1):
            e0 = abs(abs(smallestEigen)-trueEigen)
        elif(k==2):
            e1 = abs(abs(smallestEigen)-trueEigen)
        elif(k==3):
            e2 = abs(abs(smallestEigen)-trueEigen)

        k = k+1
    r = math.log(e2/e1)/math.log(e1/e0)
    return x,smallestEigen,r

def eigenNumpy(A):
    return np.linalg.eig(A)

A = np.array([[2,3,2],[10,3,4],[3,6,1]])

reqEigen = np.amax(np.abs(eigenNumpy(A)[0]))

foundEigen = RayleighQuotientIteration(A,reqEigen)
print("Rayleigh Quotient Iteration :")
print("The found eigenvalue is :",foundEigen[1])
print("The corresponding eigenvector is :",foundEigen[0])
print("The convergence rate is : ",foundEigen[2])

numpyRes = eigenNumpy(A)
print("Numpy eigenvalues and eigenvectors :")
print("The eigenvalues are ", numpyRes[0])
print("The corresponding eigenvector columns are \n", numpyRes[1])