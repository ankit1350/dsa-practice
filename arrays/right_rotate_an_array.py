class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        d=k%n
        self.reverse(0,n,nums)
        self.reverse(0,d,nums)
        self.reverse(d,n,nums)
        
    def reverse(self,i,n,a):
        if i>=n:
            return
        a[i],a[n-1]=a[n-1],a[i]
        self.reverse(i+1,n-1,a)
        return a

        
        
arr=list(map(int,input("enter array elements:").split()))
k=int(input("enter the number of elements to rotate:"))
n=len(arr)
d=k%n
a=rotate(arr,d,n)
print(a)