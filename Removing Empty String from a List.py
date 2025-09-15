#Removing empty strings from a list
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
j = 0
print("List Before = ",arr)
while('' in arr): #important step
        arr.remove('')
print("List After = ",arr)
