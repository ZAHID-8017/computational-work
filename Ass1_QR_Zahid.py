import numpy as np
A1=np.array([[5,-2],[-2,8]])
Q1,R1=np.linalg.qr(A1)
print(A1)
print(Q1)
#print(R1)
Q_T=np.transpose(Q1)
print(Q_T)
I=np.matmul(Q1,Q_T)
print(I)
eigval,eigvec = np.linalg.eigh(A1)
print("eigval:", eigval)
print(eigvec)
i=0
flag=1
while(flag==1):
    Q1,R1=np.linalg.qr(A1)
    A2=np.matmul(R1,Q1)
    Q1,R1=np.linalg.qr(A2)
    A1=A2
    i=i+1

print(A2)
    
