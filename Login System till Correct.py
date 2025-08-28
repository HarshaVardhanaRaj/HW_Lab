import sys
uid = ""
pswrd = ""
while(uid!="admin" or pswrd!="123"):
    uid = input("Enter your username: ")
    pswrd = input("Enter your password: ")
    if(uid=="admin" and pswrd=="123"):
        print("Login Successful.")
        sys.exit(0)
    else:
        print("Wrong UID or Password. Try again.")

