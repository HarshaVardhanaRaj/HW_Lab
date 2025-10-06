def largest_of_3(a,b,c):
    if(a>b and a>c):
        return(a)
    elif(b>a and b>c):
        return(b)
    else:
        return(c)
x = float(input("Enter 1st num: "))
y = float(input("Enter 2nd num: "))
z = float(input("Enter 3rd num: "))
largest = largest_of_3(x,y,z)
print("Largest =",largest)
