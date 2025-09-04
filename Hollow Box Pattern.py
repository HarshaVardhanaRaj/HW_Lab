#Hollow Box Pattern

for i in range(1,6,1):
    if(i==1 or i==5):
        for j in range(1,6,1):
            print("*", end=" ")
        print()
    else:
        for j in range(1,6,1):
            if(j==1 or j==5):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
           
