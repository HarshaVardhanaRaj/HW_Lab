x = float(input("Enter Class X Percentage: "))
xii = float(input("Enter Class XII Percentage: "))
ug_cgpa = float(input("Enter UG CGPA: "))
ug_stream = input("Enter your attended UG Stream: ")
pg_stream = input("Enter your preferred PG Stream: ")
if(pg_stream!=ug_stream):
    print("Since you are preferring a different PG Program your CGPA is reduced by 1")
    ug_cgpa-=1
    print("Your considered CGPA =",ug_cgpa)
print("Required 10th Percentage = 75 \t Your percentage =",x)
print("Required 12th Percentage = 75 \t Your percentage =",xii)
print("Required CGPA in UG = 7.5 \t Your CGPA =",ug_cgpa)
if(x>=75 and xii>=75 and ug_cgpa>=7.5):
    print("You are eligible for the preferred PG course.")
else:
    print("You are ineligible for the preferred PG course.")
