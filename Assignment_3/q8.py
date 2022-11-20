import numpy as np
import math
def RayleighQuotientIteration(A,trueEigen):
    k =0
    e0,e1,e2 = 0,0,0
    x = np.array([0,0,1])
    smallestEigen = 0
    sigma = 0
    while(k<10000):
        sigma = np.matmul(np.transpose(x),np.matmul(A,x))/np.matmul(np.transpose(x),x)
        y = np.linalg.solve(A-sigma*np.identity(3),x)
        x = y/np.linalg.norm(y,np.inf)
        smallestEigen = np.linalg.norm(y,np.inf)
        smallestEigen = 1/smallestEigen + sigma
        if(k==0):
            e0 = abs(abs(smallestEigen)-trueEigen)
        elif(k==1):
            e1 = abs(abs(smallestEigen)-trueEigen)
        elif(k==2):
            e2 = abs(abs(smallestEigen)-trueEigen)

        k = k+1
    r = math.log(e2/e1)/math.log(e1*e0)
    return smallestEigen,x,r

def eigenNumpy():
    A = np.array([[2,3,2],[10,3,4],[3,6,1]])
    return np.linalg.eig(A)

reqEigen = np.amin(np.abs(eigenNumpy()[0]))
print("The required eigen value magnitude is :",reqEigen)
A = np.array([[2,3,2],[10,3,4],[3,6,1]])
foundEigen = RayleighQuotientIteration(A,reqEigen)
print("The smallest magnitude eigenvalue is :",foundEigen[0])
print("The corresponding eigenvector is :",foundEigen[1])
print("The convergence rate is : ",foundEigen[2])
