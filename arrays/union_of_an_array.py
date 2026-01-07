arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n1=len(arr1)
n2=len(arr2)
i=j=0
arr=[]
while(i<n1 and j<n2):
    if arr1[i]<=arr2[j]:
        if arr1[i] not in arr:
            arr.append(arr1[i])
        i+=1
    else:
        if arr2[j] not in arr:
            arr.append(arr2[j])
        j+=1
while (j<n2):
    if arr2[j] not in arr:
        arr.append(arr2[j])
    j+=1
while(i<n1):
    if arr1[i] not in arr:
        arr.append(arr1[i])
    i+=1
print(arr)

'''arr=[]
for i ,x in enumerate (arr1):
    if x  not in arr:
        arr.append(x)
for i ,x in enumerate (arr2):
    if x  not in arr: 
        arr.append(x)
print(arr)'''
'''s=set()
for i in range(len(arr1)):
    s.add(arr1[i])
for i in range(len(arr2)):
    s.add(arr2[i])
l=list(s)
print(l)'''