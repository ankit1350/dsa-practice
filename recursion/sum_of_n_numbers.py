n=int(input("enter an integer:"))
def summation(i,sum):
    if(i<1):
        print(sum)
        return
    summation(i-1,sum+i)
summation(n,0)

def summation1(n):
    if(n==0):
        return 0
    return n+summation1(n-1)
print(summation1(n))