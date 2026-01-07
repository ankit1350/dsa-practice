def rotate(nums,k,n):
    n=len(nums)
    d=k%n
    reverse(0,n,nums)
    reverse(0,d,nums)
    reverse(d,n,nums)
    return nums
        
def reverse(i,n,a):
    if i>=n-1:
        return
    a[i],a[n-1]=a[n-1],a[i]
    reverse(i+1,n-1,a)
    return a

arr=list(map(int,input("enter array elements:").split()))
k=int(input("enter the number of elements to rotate:"))
n=len(arr)
d=k%n
a=rotate(arr,d,n)
print(a)