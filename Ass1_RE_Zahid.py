import numpy as np
import math
A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])
x_tr = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163
                 ])
x = np.zeros(5 , dtype=float)
x1 = np.zeros((5,5))
r = np.zeros((5,5), dtype=float)
z = np.zeros(5)
print(A)
print(b)
print(x)
count=0
w=1.25
x_n = np.zeros(5)
flag=1
while(flag==1):
    i=0
    while(i<=4):
        j = 0
        while (j<=i-1):
            x1[i,j]=x_n[j]
            j=j+1
        j=i
        while(j<=4):
            x1[i,j]=x[j]
            j=j+1
        r[i]=b-np.matmul(A,x1[i])
        x_n[i]=x[i]+w*r[i,i]/A[i,i]
        i=i+1
        #print(x_n)
    n=0
    while(n<=4):
        z[n]=abs(x_tr[n]-x_n[n])
        n=n+1
    #print(z)
    n=0
    flag=0
    while(n<=4):
        if(abs(z[n])>.01):
            flag=1
        n=n+1
    n=0
    while(n<=4):
        x[n]=x_n[n]
        n=n+1

print(x_n)
        
      
    
        
        
        
        
        
   
        


  
    
        
        
