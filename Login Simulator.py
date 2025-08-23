uid = input("Enter your UserID: ")
pswrd = input("Enter your Psssword: ")
if(uid=="admin" and pswrd=="123"):
    print("Login Successful.")
elif(uid=="admin" and pswrd!="123"):
    print("Wrong Password.")
else:
    print("UID not found.")