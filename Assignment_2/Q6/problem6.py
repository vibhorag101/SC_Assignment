import scipy.linalg as sp
import numpy as np
import matplotlib.pyplot as plt

def solveQR(k,A,b):
    Q,R = np.linalg.qr(A)
    x = sp.solve_triangular(R, np.matmul(Q.T, b))
    return x

def solveNormal(k,A,b):
    Ata = np.matmul(A.T, A)
    Atb = np.matmul(A.T, b)
    x = np.linalg.solve(Ata, Atb)
    return x

for i in range(6,16):
    k=i
    A = np.array([[1, 1], [10**(-k), 0],[0, 10**(-k)]])
    b = np.array([-(10**(-k)), 1+10**(-k),1-10**(-k)])
    print("k = ", i)
    print("Solution using QR: ", solveQR(i,A,b))

for i in range(6,16):
    k=i
    A = np.array([[1, 1], [10**(-k), 0],[0, 10**(-k)]])
    b = np.array([-(10**(-k)), 1+10**(-k),1-10**(-k)])
    print("k = ", i)
    try:
        print("Solution using Normal: ", solveNormal(i,A,b))
    except:
        print("Error Singular Matrix")