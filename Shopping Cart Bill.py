import sys
bill = 0
while(True):
    price = float(input("Enter price of item, or enter 0 when done: "))
    if(price!=0):
        bill+= price
    else: 
        print("Total Bill = Rs.",bill)
        sys.exit(0)