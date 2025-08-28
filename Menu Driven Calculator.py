import sys
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
while(True):
    ch = int(input("Enter 1 to Add, 2 to Subtract, 3 to multiply, 4 to divide, or 5 to exit: "))
    if(ch==1):
            print(a,'+',b,'=',(a+b))
    elif(ch==2):
            print(a,'-',b,'=',(a-b))
    elif(ch==3):
            print(a,'x',b,'=',(a*b))
    elif(ch==4):
            print(a,'/',b,'=',(a/b))
    elif(ch==5):
            print("Operation Over.")
            sys.exit(0)
    else: 
            print("Invalid Option")