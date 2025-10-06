#Calculator

def add(*nums):
    s = 0
    for i in nums:
        s+=i
    return(s)

def prod(*nums):
    p = 1
    for i in nums:
        p*=i
    return(p)

def diff(a,b):
    return(abs(a-b))

def div(a,b):
    return(a/b)

def quo(a,b):
    return(a//b)

def rem(a,b):
    return(a%b)

def fact(a):
    f = 1
    for i in range(a,0,-1):
        f*=i
    return(f)

print(add(1,2,3,4,5))
print(prod(1,2,3,4,5))
print(diff(3,4))
print(div(2,3))
print(quo(2,3))
print(rem(2,3))
print(fact(5))
