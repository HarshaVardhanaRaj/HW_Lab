#Max and Min of a List
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
max=arr[0] ; min=arr[0]
for i in range(0,l,1):
    if(arr[i]>max):
        max=arr[i]
    if(arr[i]<min):
        min=arr[i]
print("Largest Number =",max)
print("Smallest Number =",min)
