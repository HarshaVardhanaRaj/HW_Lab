import sys
c = 0
while(c<=3):
    pin = int(input("Enter your ATM PIN: "))
    if(pin==1234):
        print("Access Granted")
        sys.exit(0)
    else:
        print("Wrong PIN. You have",(3-c),"attempts left.")
        c+=1
print("You have exhausted the number of Trials. Your Card is Blocked.")
