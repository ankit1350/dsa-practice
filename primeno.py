import math
n=int(input("enter number:"))
cnt=0
for i in range(1,int(math.sqrt(n))+1):
    if(n%i==0):
        cnt+=1
        if ((n/i)!=i):
            cnt+=1
if cnt==2:
    print("prime")
else:
    print("not prime")

    
        
