#Count occurence
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
obj = input("Enter element whose occurence is needed: ")
c = arr.count(obj)
print(obj,"occurs",c,"times in the List.")
