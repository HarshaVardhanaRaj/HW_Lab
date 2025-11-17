class Student:

    def __init__(self):
        self.name = ""
        self.roll = 0
        self.marks = 0


    def accept(self):
        print("Input the Student Details: ")
        self.name = input("Name = ")
        self.roll = int(input("Roll = "))
        self.marks = int(input("Marks = "))


    def display(self):
        print("\nEntered Student Details: ")
        print("Name =",self.name)
        print("Roll =",self.roll)
        print("Marks =",self.marks)


    def grade(self):
        print("\n")
        if(self.marks>=90):
            print('A',end=' ')
        elif(self.marks<90 and self.marks>=75):
            print('B',end=' ')
        elif(self.marks<75 and self.marks>=50):
            print('C',end=' ')
        else:
            print('F',end=' ')
        print("Grade")


s1 = Student()
s1.accept()
s1.display()
s1.grade()
