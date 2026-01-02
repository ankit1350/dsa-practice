n=int(input("enter a  number:"))
a=n
s=len(str(n))
sum=0
while(n>0):
    remainder=n%10
    n=int(n/10)
    sum=sum+((remainder)**s)
if sum==a:
     print(True)
else:
    print(False)