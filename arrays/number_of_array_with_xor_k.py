from collections import defaultdict
a=[4,2,2,6,4]
k=6
xr=0
d=defaultdict(int)
d[0]=1
cnt=0
for e in a:
    xr=xr^e
    x=xr^k
    cnt+=d[x]
    d[xr]+=1
print(cnt)