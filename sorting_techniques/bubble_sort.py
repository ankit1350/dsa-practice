arr = list(map(int, input().split()))
n=len(arr)
for i in range(n-1,0,-1):
    swapped=0
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=1
    if swapped==0:
        break
print(arr)


