import numpy as np
import scipy.linalg as qr
def QRIteration(A):
    k = 0
    Q,R = qr.qr(A)
    n = np.shape(A)[0]
    while(k<10000):
        sigma = A[n-1,n-1]
        Q,R = qr.qr(A-sigma*np.identity(n))
        A = np.matmul(R,Q) + sigma*np.identity(n)
        k = k+1
    return A

def eigenNumpy(A):
    return np.linalg.eig(A)

A = np.array([[2,3,2],[10,3,4],[3,6,1]])
print("For matrix in Q6 :")
print("Eigen values using QR Iteration : ",np.diag(QRIteration(A)))
print("Eigen values using numpy : ",eigenNumpy(A)[0])

A = np.array([[6,2,1],[2,3,1],[1,1,1]])
print("For matrix in Q7 :")
print("Eigen values using QR Iteration : ",np.diag(QRIteration(A)))
print("Eigen values using numpy : ",eigenNumpy(A)[0])
