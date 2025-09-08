# sum of series
n = int(input("n = "))
s = 0
for i in range(1,n+1,1):
    t = (i*i)/i
    s = s + t
print("Sum of series =",s)
    
