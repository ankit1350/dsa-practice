
from cmath import sqrt
import math
n=int(input("enter a number:"))


'''
for i in range(1,n+1):
    if n%i==0:
        print(i,end=",")
    
another program which will run till only upto its square root to get the factors'''
l=[]
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        l.append(i)
        if (n/i!=i):
            l.append(int(n/i))
print(sorted(l))