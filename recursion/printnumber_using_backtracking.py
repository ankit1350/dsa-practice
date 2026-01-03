n=int(input("enter integer :"))
def prinT(i,n):
    if (i>n):
        return
    prinT(i+1,n)
    print(i)


def Print(i,n):
    if(i<1):
        return
    Print(i-1,n)
    print(i)

def menu():
    while True:
        print("chose the option")
        print("1.N to 1")
        print("2.print 1 to N")
        print("3.Exit")
        choice=int(input())
        if choice==1:
            prinT(1,n) 
        elif choice==2:
            Print(n,n) 
        else:
            print("chose from the options above")
            break
menu()