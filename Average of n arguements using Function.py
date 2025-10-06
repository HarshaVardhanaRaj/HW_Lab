def average(*nums):
    s = 0 ; c = 0
    for i in nums:
        s+=i
        c+=1
    return(s/c)
avg = average(1,2,3,4,5,6,7,8,9)
print("Average =",avg)
