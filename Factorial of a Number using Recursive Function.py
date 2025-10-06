# factorial of a number using recursion
f = 1
def fact(n):
    if(n==0):
        return 1
    f = n * fact(n-1)
    return f

num = int(input("Enter an integer: "))
print("Factorial of",num,"=",fact(num))
