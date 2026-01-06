arr=list(map(int,input().split()))
n=len(arr)
l=arr[0]
for i in range(n):
    if arr[i]>l:
        l=arr[i]
print(l)