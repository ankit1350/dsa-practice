'''
"Kadane's algorithm:
initialize max,sum
traverse all numbers add it to the sum , if the sum is negative: put sum=0
if it is positive, carry it forward
if sum>max then update max=sum
'''

class Solution:
    def maxSubArray(self, nums):
        n=len(nums)
        max1=nums[0]
        sum=0
        for i in range(n):
            sum+=nums[i]
            if sum>max1:
                max1=max(max1,sum)
                ansStart=start
                ansEnd=i
            if sum<0:
                sum=0
                start=i+1
        '''for i in range(ansStart,ansEnd+1):  #when asked to print that sub array
            print(nums[i],end=" ")'''
        return max1

nums=[-2,1,-3,4,-1,2,1,-5,4]
sl=Solution()
a=sl.maxSubArray(nums)
print(a)