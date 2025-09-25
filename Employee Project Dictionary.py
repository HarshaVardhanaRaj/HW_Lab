employee_list = {'A':'Andrew' , 'B':'Brandon' ,'C':'Cayley' , 'D':'Darren'}
prj = input("Enter Project Name: ")
if prj in employee_list:
    print("Employee associated with Project",prj,"=",employee_list[prj])
else:
    print("Project not found.")
