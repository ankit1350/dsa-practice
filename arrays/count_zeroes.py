#User function Template for python3

class Solution:
    def countZeroes(self, arr):
        # code 
        a=[]
        n=len(arr)
        for i in range(n):
            if arr[i]==0:
                a.append(0)
                i=i+1
        return len(a)
