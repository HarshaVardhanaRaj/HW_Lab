l = int(input("Enter no. of Elements: "))
arr = []
for i in range(l):
    arr.append(int(input("Enter an integer: ")))
print("Original List: ",arr)
arr = [x for x in arr if x%2==0]
print("Even numbers are: ",arr)
