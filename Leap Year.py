year = (input("Enter a year: "))
y = int(year[-2:])
if(y%4==0):
    print(year,"is a Leap Year.")
else:
    print(year,"is Not a Leap Year.")
