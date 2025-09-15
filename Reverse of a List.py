#Reversing a list
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
print("Reverse of List: ")
print("[", end="")
for i in range(l-1, -1, -1):
    print(arr[i], end="")
    if(i!=0):
        print(",", end="")
print("]")
