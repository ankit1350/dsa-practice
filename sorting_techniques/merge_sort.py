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



