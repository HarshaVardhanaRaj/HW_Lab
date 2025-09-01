s = 0 ; a = 0 ; i = 1
n = int(input("How many numbers?: "))
while(i<=n):
    num = int(input("Enter a num: "))
    s = s+num
    i+=1
a = s/n
print("Sum of",n,"numbers =",s)
print("Avg of",n,"numbers =",a)
