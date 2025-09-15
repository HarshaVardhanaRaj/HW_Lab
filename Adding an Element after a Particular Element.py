#adding an element after a particular element
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
el = input("Element to be added = ")
ind = input("After what element?: ")
ind = arr.index(ind)
arr.insert(ind+1,el)
print("Modified List =",arr)
