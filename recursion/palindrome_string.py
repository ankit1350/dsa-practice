s=input("enter a string to check palindrome:")
n=len(s)
def palindrome(i,s):
    if(i>=2):
        return True
    if(s[i]!=s[n-i-1]):
        return False
    return palindrome(i+1,s)
print(palindrome(0,s))