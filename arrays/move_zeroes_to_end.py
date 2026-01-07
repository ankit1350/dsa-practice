def moveZeroes(nums):
        j=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        for i in range(j+1,n):
            if nums[i]!=0 and nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums

'''
brute force method is just to initialize temp array first store non zero elements and then the zeroes
def move_zeroes_to_end(nums):
    a=[]
    n=len(nums)
    cnt=0
    for i in range(n):
        if nums[i]!=0:
            a.append(nums[i])
        else:
            cnt+=1
    
    for i in range(cnt):
        a.append(0)
    return a
    '''
a=[1,0,0]
b=moveZeroes(a)
print(b)