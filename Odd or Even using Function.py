def even_odd (n):
    if(n%2==0):
        return("Even")
    else:
        return("Odd")
num = int(input("Enter a number: "))
res = even_odd(num)
print(num,"is",res)
