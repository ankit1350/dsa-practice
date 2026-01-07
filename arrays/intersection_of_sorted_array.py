arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
n1=len(arr1)
n2=len(arr2)
i=j=0
arr=[]
while(i<n1 and j<n2):
    if arr1[i]<arr2[j]:
        i+=1
    elif arr2[j]<arr1[i]:
        j+=1
#agar list empty hai
#YA last added element current element se different hai,
#tabhi add karo.
    else:
        if not arr or arr[-1] != arr1[i]:
            arr.append(arr1[i])
        i+=1
        j+=1

print(arr)

'''for i in range(n1):
        if arr1[i] in arr2 :           #time complexity is n square for this brute force method
            if arr1[i] not in arr:
                arr.append(arr1[i])'''
        
        
    