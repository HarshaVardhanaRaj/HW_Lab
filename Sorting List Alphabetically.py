#Arranging Alphabetically

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for i in range(0,len(students)-1,1):
    for j in range(0,len(students)-1,1):
        if(students[j][0]>students[j+1][0]):
            temp = students[j+1][0]
            students[j+1][0] = students[j][0]
            students[j][0] = temp
        else:
            continue
print(students)
