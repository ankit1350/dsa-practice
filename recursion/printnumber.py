n=int(input("enter integer :"))
def prinT(i,n):
    if (i>n):
        return
    print(i)
    prinT(i+1,n)


def Print(i,n):
    if(i<1):
        return
    print(i)
    Print(i-1,n)

def menu():
    while True:
        print("chose the option")
        print("1.print 1 to N")
        print("2.N to 1")
        print("3.Exit")
        choice=int(input())
        if choice==1:
            prinT(1,n)
            
        if choice==2:
            Print(n,n)
            
        else:
            print("chose from the options above:")
            break
menu()