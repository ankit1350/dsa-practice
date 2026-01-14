##1.
def leader0(arr):
    n=len(arr)
    a=[]
    maxi=0
    for i in range(n-1,-1,-1):
        if arr[i]>maxi:
            maxi=arr[i]
            a.append(arr[i])
    return a
print(leader0([10,22,12,3,0,6]))
'''##2.
def leader(arr):
    n=len(arr)
    a=[]
    for i in range(n-1):
        for j in range(i,n-1):
            if arr[j]>arr[i]:
                a.append(arr[j])
    a.append(arr[n-1])
    return a
print(leader([10,22,12,3,0,6]))
##3.
def leader1(arr):
    n=len(arr)
    a=[]
    for i in range(n-1):
        if arr[i]>max(arr[i+1:]):
            a.append(arr[i])
    a.append(arr[n-1])
    return a
print(leader1([10,22,12,3,0,6]))'''