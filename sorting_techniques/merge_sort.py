def merge_sort(arr):
    if len(arr) <= 1:
    #base condition
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    #two pointers for both arrays 
    #if element in left array at ith position is less than the element at the jth
    #position in the right array then append the left element else append the right one.
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])#if j exceeds the length but there are elements still present in the left array
    result.extend(right[j:])
    return result


arr = list(map(int, input().split()))
arr = merge_sort(arr)
print(arr)



'''arr=list(map(int,input().split()))
n=len(arr)
low=0
high=n-1
def merge_sort(arr,low,high):
    if(low>=high):
        return
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and right<=high):
        if(arr[left]<arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
merge_sort(arr,low,high)
print(arr)'''