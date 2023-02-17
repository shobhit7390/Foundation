# Recursion

#factorial(n)=n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(7))
print(factorial(5))


# Fibonacci series

# f0=1   f1=1
# f(n)=f(n-1)+f(n-2)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

a=int(input("Enter a number :"))

for i in range(a):
    print(fibonacci(i),end=" ")
