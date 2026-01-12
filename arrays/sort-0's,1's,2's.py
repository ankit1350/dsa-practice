#Dutch National Flag algorithm:
'''
low → end of the region containing 0s
mid → current element being processed
high → start of the region containing 2s

If the current element is 0, swap it to the front and move low and mid
If it is 1, leave it in the middle and move mid
If it is 2, swap it to the end and move high
'''
n=len(arr)
low=mid=0
high=n-1
while(mid<=high):
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        mid+=1
        low+=1
    elif arr[mid]==1:
        mid+=1
    elif arr[mid]==2:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
    