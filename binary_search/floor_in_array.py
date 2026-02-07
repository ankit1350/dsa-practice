#floor value : the largest number in array that is less than or equal to the target.
def floor(arr,target):
    n=len(arr)
    low=0
    ans=-1
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
if __name__=='__main__':
    arr=[1,3,4,5,6,7]
    print(floor(arr,5))