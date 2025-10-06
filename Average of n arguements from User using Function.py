#Average of n numbers from the user using a function

def avg(*nums):
    s = 0 ; c= 0
    for i in nums:
        s+=i
        c+=1
    return(s/c)
numbers = list()
n = int(input("How many nums?: "))
print("Enter",n,"nums: ")
for i in range (0,n,1):
    inp = float(input("Num = "))
    numbers.append(inp)
a = avg(*numbers)
print("Average =",a)
    
