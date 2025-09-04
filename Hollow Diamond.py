#Hollow Diamond.................

for i in range(1,6,1):
    for j in range(1,6,1):
        if(i==1 or i==5):
            if(i+j==4):
                print("*", end=" ")
        elif(i==3):
            if(i+j==4 or i+j==8):
                print("*", end=" ")
        elif(i==2 or i==4):
            if(i+j==4 or i+j==6):
                print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
