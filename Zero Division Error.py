# 0 division error

'''a = 5
b = 0
c = a/b
print (c)

'''

try:
    a = 5
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Denominator cannot be zero")
