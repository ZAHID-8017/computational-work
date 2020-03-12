import numpy as np

L_0=0
A = np.array([[2,-1,0] , [-1,2,-1] , [0,-1,2]],dtype=float)
X0 = np.array([1,1,1])

flag=1
while(flag==1):
    X1=np.matmul(A,X0)
    X2=np.matmul(A,X1)
    L_1=np.matmul(X2,X0)/np.matmul(X1,X0)
    e=(L_1-L_0)/L_1
    flag=0
    if(e>0.01):
        flag=1
        
       
    X0=X1
    L_0=L_1
    

print(X1)
print("dominant eigenval:",L_0)
eigval,eigvec = np.linalg.eigh(A)
print(eigval)
print(eigvec)
z=np.dot(A,X0)
print(z)





