'''
"Moore's voting algorithm":
select one element and check other incoming element
if the incoming element is same as the pre element then increase the counter
if it's not the same then decrease the counter
as  the counter becomes equals to zero , restart the process for diff element
'''
n=len(arr)
for i in range(n):
    if cnt==0:
        cnt=1
        element=arr[i]
    else:
        if arr[i]==element:
            cnt+=1
        else:
            cnt-=1
'''
check this for loop only when the problem says:
if the majority element not exists return -1
otherwise no need of this for loop , just simply return the last element above
'''
count=0
for i in range(n):
    if nums[i]==element:
        count+=1
if count>(n/2):
    print(element)
print("-1")