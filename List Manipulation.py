#List Manipulation

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
print("Initial List: ",arr)
arr[1] = 200
print("After changing 2nd element: ",arr)
arr.append(600)
print("After appending 600 to the last: ",arr)
arr.insert(2,300)
print("After inserting 300 at index 2: ",arr)
arr.remove(600)
print("After removing 600: ",arr)
arr.pop(0)
print("After removing element at index 2: ",arr)
