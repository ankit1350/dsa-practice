class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        def fxn(n,r):
            res=1
            for i in range(r):
                res=res*(n-i)
                res=res/(i+1)
            return int(res)
        for i in range(numRows):
            s=[0]*(i+1)
            for j in range(i+1):
                s[j]=fxn(i,j)
            a.append(s)
        return a