i = 0 ; arr=[]
while(True):
    element = input("Enter Element or 'QUIT' exit: ")
    if(element=='QUIT'):
        print("List is completed.")
        break
    else:
        arr.append(element)
        i+=1
l = len(arr)
if(l<3):
    print("3rd element doesn't exist.")
else:
    print("3rd element =",arr[2])
print("Length of List =",l)
if(l==0):
    print("List is empty.")
else:
    print("List is not empty.")
