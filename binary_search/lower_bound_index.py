#the lowest index number which is just greater than or equal to the target
def lower (arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
if __name__ == "__main__":
    arr=[1,2,4,5,8,9,12,16]
    print(lower(arr,1))