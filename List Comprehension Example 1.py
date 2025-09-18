# List Comprehension Example 1
num = []
for i in range(5):
    num.append(int(input("Enter num: ")))
print("Before adding 5: ")
print("List = ",num)
print("After adding 5 to each element: ")
num = [x+5 for x in num]
print(num)
