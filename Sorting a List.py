#Sorting a List
i = 0 ; arr=[]
while(True):
    element = int(input("Enter Element or 0 exit: "))
    if(element==0):
        print("List is completed.")
        break
    else:
        arr.append(element)
        i+=1
l = len(arr)
arr.sort()
print("Sorted array =",arr)
