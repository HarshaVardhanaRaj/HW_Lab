#without using a 3rd variable

a = int(input("a = "))
b = int(input("b = "))
print("Before Swapping: ")
print("a =",a,"and b =",b)
print("After Swapping:")
a = a+b
b = a-b
a = a-b
print("a =",a,"and b =",b)
