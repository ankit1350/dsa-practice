n=int(input("enter number of times to print:"))
name=input("enter the name:")
def fun(i,n,name):
    if(i>n):
        return
    print(name)
    fun(i+1,n,name)
fun(1,n,name)