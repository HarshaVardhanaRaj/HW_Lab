import sys
units = int(input("Enter units consumed: "))
if(0<=units<=100):
    bill = 5*units
elif(100<units<=200):
    bill = 5*(100) + 7*(units-100)
elif(units>200):
    bill = 5*(100) + 7*(100) + 10*(units-200)
else:
    print("Invalid Input")
    sys.exit(0)
print("Bill = Rs.",bill)