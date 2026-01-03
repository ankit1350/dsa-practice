n=int(input("enter the integer to find the nth fibonacci number:"))

'''def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(n))

time complexity is very much since many factorials are calculated multiple times.'''


memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(n))
#it is efficient since it reduces time complexity by making a 
# dictionary storing the fibonacci values already created