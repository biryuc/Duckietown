import numpy as np
A = np.array([[1,2,6],[8,5,6],[7,8,9]],dtype=int)
print(A)
determenant = np.linalg.det(A)
print(determenant)
if determenant < 0:
    print("Error")
else:
    B = np.linalg.inv(A)
    print(B)
    C = np.matmul(A,B)
    print(C)