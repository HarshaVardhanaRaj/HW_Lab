num = int(input("Enter a number: "))
og = num ; s = 0
while(num>0):
    d = num%10
    s = s + d
    num = num//10
print("Sum of digits of",og,"=",s)
