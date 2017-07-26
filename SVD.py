import numpy as np
from numpy import linalg as la

A = np.random.randn(10000, 100)
#A = np.mat([[0,1,2,3], [4,5,6,7], [8,9,10,11]])

U, s, V = la.svd(A, full_matrices=True)

print(U)
print(s)
print(V)