l = int(input("Enter no. of Elements: "))
arr = []
for i in range(l):
    arr.append(int(input("Enter an integer: ")))
print("Original List: ",arr)
sqrs = [x**2 for x in arr]
cubes = [x**3 for x in arr]
even = [x for x in arr if x%2==0]
print("Squares:",sqrs)
print("Cubes:",cubes)
print("Even nos:",even)
