#sets the min index and check for the smallest element in the array i+1,n . if any element smaller 
#than the element at the min index is found then assign min_index to that element 
#and swap it.

arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

print(arr)