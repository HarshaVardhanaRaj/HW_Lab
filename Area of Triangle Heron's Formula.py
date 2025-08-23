a = float(input("Length of side a = "))
b = float(input("Length of side b = "))
c = float(input("Length of side c = "))
s = (a+b+c)/2
area = pow(s*(s-a)*(s-b)*(s-c), 0.5)
print("Area of Triangle = ")