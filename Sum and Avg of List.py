#Sum and Average of a List
i = 0 ; arr=[] ; s=0
while(True):
    element = int(input("Enter Element or '0' to exit: "))
    if(element==0):
        print("List is completed.")
        break
    else:
        arr.append(element)
        s = s + arr[i]
        i+=1
l = len(arr)
print("Sum of List =",s)
print("Avg of List =",(s/l))
