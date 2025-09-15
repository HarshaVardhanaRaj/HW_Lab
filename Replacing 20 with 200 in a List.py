#Replace iten with a new item
i = 0 ; arr=[]
while(True):
    element = input("Enter Element or 'QUIT' exit: ")
    if(element=='QUIT'):
        print("List is completed.")
        break
    else:
        arr.append(element)
        i+=1
print("Original Array =",arr)
l = len(arr)
for i in range(0,l,1):
    if(arr[i]=='20'):
        print("Element 20 found. Replaced with 200")
        arr[i]='200'
        break
print("Modified Array =",arr)
