import numpy as np
import math
A = np.array([[0.2, 0.1, 1, 1, 0], [0.1, 4, -1, 1, -1], [1, -1, 60, 0, -2], [1, 1, 0, 8, 4], [0, -1, -2, 4, 700]])
b = np.array([1, 2, 3, 4, 5])
x_tr=np.array([7.859713071, 0.422926408, -0.073592239, -0.540643016, 0.010626163])
x=np.zeros(5, dtype=float)
r=b-np.matmul(A,x)
p=r
temp=np.matmul(np.transpose(r),r)
flag=1
count=0
while(flag==1):
    Ap=np.dot(A,p)
    t=temp/(np.matmul(np.transpose(p),Ap))
    x=x+t*p
    r=r-t*Ap
    temp1=np.matmul(np.transpose(r),r)
    p=r+(temp1/temp)*p
    temp=temp1
    flag=0
    i=0
    z=x_tr-x
    while(i<=4):
        if(abs(z[i])>0.01):
            flag=1
        count=count+1
        i=i+1
print(x)
print("count: \n", count)

    

