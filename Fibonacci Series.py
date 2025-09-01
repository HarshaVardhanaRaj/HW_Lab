a = 0 ; b = 1 ; i = 1
n = int(input("How many nums of the Fibonacci series do you need?: "))
print(a, end=", ")
print(b, end=", ")
while(i<=n-2):
    c = a+b
    print(c, end=", ")
    a=b
    b=c
    i+=1
