import time 
import numpy as np
start = time.process_time()
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
print(A)
A_T=np.transpose(A)
print(A_T)
C=np.matmul(A_T,A)
D=np.matmul(A,A_T)
print(C)
print(D)
eiv1,V=np.linalg.eigh(C)
eiv2,U=np.linalg.eigh(D)
print("eigenvalue1: \n",eiv1)
print("eigenvector1: \n",V)
print("eigenvalue2: \n",eiv2)
print("eigenvector2: \n",U)
eiv1=eiv1.argsort()[::-1]
eiv2=eiv2.argsort()[::-1]
U=U[:,eiv2]
V=V[:,eiv1]
print("U{i,j]: \n",U)
print("V{i,j]: \n",V)
U_T=np.transpose(U)
S1=np.matmul(U_T,A)
S=np.matmul(S1,V)
print("S:",S)
u,s,v=np.linalg.svd(A)
print("svd using numpy: \n")
print("s: \n",s)
print("v: \n",v)
print("u: \n",u)
print("time required: \n" ,time.process_time() - start)




    
