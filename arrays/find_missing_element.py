'''
x^x=x and x^0=x
apply above logic
xor1 will have n consecutive numbers in xor
xor2 will have all elements of nums in xor
and when we do xor1^xor2 all the elements that are present in both will make it zero and the one 
left along with zero will be returned as the desired value.
'''
def missingNumber(nums):
    n=len(nums)
    xor1=xor2=0
    for i in range(n):
        xor2=xor2^nums[i]
        xor1=xor1^(i+1)
    return xor1^xor2