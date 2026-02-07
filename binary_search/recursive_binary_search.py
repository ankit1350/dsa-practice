def binary_search(low,high,arr,key):
    if(low==high):
        if arr[low]==key:
            return low
        return -1
    else:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binary_search(mid+1,high,arr,key)
        else:
            return binary_search(low,mid-1,arr,key)
arr=[1,5,9,11,25,30,36,88]
a=binary_search(0,7,arr,30)
print(a)