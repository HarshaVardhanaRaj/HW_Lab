#check input name
import sys
name = sys.argv[1]

name = name.lower()
if(name=='rahul'):
    print("Access Denied. Quit the Program.")
else:
    print("Welcome,",name)
