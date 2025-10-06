def largest_of_n(*nums):
    lar = nums[0] ; sml = nums[0] ; l = len(nums)
    for i in range(0,l,1):
        for i in range(0,l,1):
            if(nums[i]>lar):
                lar = nums[i]
            elif(nums[i]<sml):
                sml = nums[i]
    return(lar,sml)
numbers = list()
n = int(input("How many nums?: "))
for i in range (0,n,1):
    inp = float(input("Num = "))
    numbers.append(inp)
largest,smallest = largest_of_n(*numbers)       #important step
print("Largest =",largest)
print("Smallest =",smallest)
