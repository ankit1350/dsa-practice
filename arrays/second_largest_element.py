'''
Traverse the array only once, check if the number is greater than the largest
if it is, then assign largest value to that number and the previous largest 
value to the second largest
if the number==largest: then check if it greater than second largest or not
if it is, then assign second_largest to it.
'''
class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        largest=arr[0]
        s_largest=-1
        for i in range(n):
            if arr[i]>largest:
                s_largest=largest
                largest=arr[i]
                
            elif arr[i]==largest:
                i+=1
            else:
                
                if arr[i]>s_largest:
                    s_largest=arr[i]
        return s_largest
