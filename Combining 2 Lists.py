#Combine 2 Lists
i = 0 ; arr1=[]
print("For List 1:")
while(True):
    element = int(input("Enter Element or 0 exit: "))
    if(element==0):
        print("List is completed.")
        break
    else:
        arr1.append(element)
        i+=1
i = 0 ; arr2=[]
print("For List 2:")
while(True):
    element = int(input("Enter Element or 0 exit: "))
    if(element==0):
        print("List is completed.")
        break
    else:
        arr2.append(element)
        i+=1
arr3 = arr1 + arr2
print(arr3)
