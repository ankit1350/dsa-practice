'''1.reverse first 'd' elements of the array
2.then reverse the elements from d to n
3. and at last reverse the whole array to get the desired result.'''
arr=list(map(int,input("enter array elements:").split()))
k=int(input("enter number of elements to rotate:"))
n=len(arr)
d=k%n
def reverse(i,n,a):
    if i>=n:
        return
    a[i],a[n-1]=a[n-1],a[i]
    reverse(i+1,n-1,a)
reverse(0,d,arr)
reverse(d,n,arr)
reverse(0,n,arr)
print(arr)




'''arr=[1,2,3,4,5]
k=int(input("enter elements to rotate by:"))
n=len(arr)
d=k%n
temp=[]
for i in range(d):
    temp.append(arr[i])
print(temp)
for j in range(d,n):
    arr[j-d]=arr[j]
print(arr)
for i in  range(n-d,n):
    arr[i]=temp[i-(n-d)]
print(arr)'''