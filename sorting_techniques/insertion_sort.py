#this sorting takes an element each time and check its correct positon with the elements present 
#to its left. If it's not in the correct position then shift all elements greater than it to the
#right and place that lesser element at its correct position.

arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1

print(arr)
'''check 2nd element with first element swap if needed
then take 3rd element and check its position with the 2nd and 1st element.
similarly in the same fashion add other elements one by one , check their relative position
and swap if needed'''