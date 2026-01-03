a=[1,2,3,4,5]
n=len(a)
def reverse(i,right,a):
    if i>=right:
        return
    a[i],a[right]=a[right],a[i]
    reverse(i+1,right-1,a)
reverse(0,n-1,a)

def reverse1(i,n,a):
    if(i>=n/2):
        return
    a[i],a[n-i-1]=a[n-i-1],a[i]
    reverse(i+1,n,a)
print(a)
