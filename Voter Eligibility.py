age = float(input("Enter your age (in years): "))
if(age>=18.0):
    print("You are eligible to vote.")
elif(0<=age<=18):
    print("You need to wait for",(18-age),"years to become eligible to vote.")