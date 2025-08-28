import sys
while(True):
    pswrd = input("Enter the password: ")
    if(pswrd=='admin'):
        print("Login successful.")
        sys.exit(0)
    else:
        print("Wrong. Try again.")