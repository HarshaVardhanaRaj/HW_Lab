import sys
c = 1
while(c<=5):
    print("Enter String",c,": ", end = "")
    s = input()
    if(len(s)>=6):
        print(s)
        print()
        c+=1
    else:
        print("String is small. Try again")
        print()
        continue
