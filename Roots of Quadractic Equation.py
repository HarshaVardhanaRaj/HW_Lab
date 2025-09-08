a = int(input("Coefficient of x^2 = "))
b = int(input("Coefficient of x = "))
c = int(input("Constant Term = "))
d = b*b - 4*a*c
print("(",a,") x^2  +  (",b,") x  +  (",c,") c = 0 has: ")
if(d>0):
    print("Real and Distinct Roots:")
elif(d==0):
    print("Real and Equal Roots:")
else:
    print("Complex Roots:")
if(d<0):
    print("(-",b,"+",pow(-d,0.5),"i) /",(2*a)," and ","(-",b,"-",pow(-d,0.5),"i) /",(2*a))
else:
    r1 = (-b + pow(d,0.5))/(2*a)
    r2 = (-b - pow(d,0.5))/(2*a)
    print(r1," and ",r2)
