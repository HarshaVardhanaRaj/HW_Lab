import sys
rad_circumference = {}
while(True):
    r = float(input("Enter Radius of a Circle or 0 to Exit: "))
    if r==0:
        for i in rad_circumference:
            print("Radius =",i,"\t\t\tCircumference =",rad_circumference[i])
        print("Program Terminated.")
        sys.exit(0)
    else:
        c = 2*3.1415*r
        rad_circumference[r] = c

