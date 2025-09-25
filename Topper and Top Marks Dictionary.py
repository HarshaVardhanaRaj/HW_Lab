student_marks_4 = {'A':[95,94,93,98],
                   'B':[85,90,85,99],
                   'C':[90,92,79,100],
                   'D':[87,91,88,95],
                   'E':[99,89,95,96]}
student_total =  {}
s = 0
for x in student_marks_4:
    l = student_marks_4[x]
    for i in range(4):
        s = s + l[i]
        student_total[x] = s
    s = 0
    print("Student =",x,"\tTotal=",student_total[x])
top = '' ; top_mark=0
for x in student_total:
    if student_total[x] > top_mark:
        top_mark = student_total[x]
        top = x
print("Topper =",top,"\tMarks =",top_mark)
