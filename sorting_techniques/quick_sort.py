def quick_sort(arr,low,high):
    if low<high:
        position=partition(arr,low,high)
        quick_sort(arr,low,position-1)
        quick_sort(arr,position+1,high)

    return arr

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while (i<j):
        while(arr[i]<=pivot and i<=high-1):
            i+=1
        while(arr[j]>pivot and j>=low+1):
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

arr=list(map(int,input().split()))
low=0
high=len(arr)-1
print(quick_sort(arr,low,high))