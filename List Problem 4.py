veg = [] ; bot_name = []
print("Enter name of 5 vegetables: ")
for i in range(0,5,1):
    val1 = input("Veg = ")
    veg.append(val1)
print("Enter their botanical name: ")
for i in range(0,5,1):
    val2 = input("Botanical name: = ")
    bot_name.append(val2)
zipped = zip(veg,bot_name)
arr = list(zipped)
for i in range(0,5,1):
    print("The botanical name of",arr[i][0],"is",arr[i][1])
