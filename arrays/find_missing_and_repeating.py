a=[4,3,2,1,1,6]
n=len(a)
x=y=0
s=(n*(n+1))/2
sq=(n*(n+1)*(2*n+1))/6
s1=0
s2=0
for e in a:
    s1+=e
    s2+=(e*e)
d=s-s1 #  y-x
ds=sq-s2  #y^2-x^2=(y-x)(y+x)   therefore, y+x=(d)/y-x
ds=ds/d
y=(d+ds)/2
x=(y-d)
print(int(x),int(y))

