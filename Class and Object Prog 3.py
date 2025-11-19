class Employee:

    def __init__(self, emp_id, name, basic_pay):
        self.emp_id = emp_id
        self.name = name
        self.basic_pay = basic_pay
        self.hra = 0.2 * basic_pay
        self.da = 0.1 * basic_pay
        self.pf = 0.05 * basic_pay
        self.net_salary = 0.0


    def calculate_salary(self):
        gross_salary = self.basic_pay + self.hra + self.da
        deductions = self.pf
        self.net_salary = gross_salary - deductions


    def display_details(self):
        print("\nEmployee Details:\n")
        print("Employee ID:",self.emp_id)
        print("Employee Name:",self.name)
        print(f"Basic Pay: {self.basic_pay : 2f}")
        print(f"HRA (20%): {self.hra : 2f}")
        print(f"DA (10%): {self.da : 2f}")
        print(f"PF (5%): {self.pf:2f}")
        print(f"Net Salary: {self.net_salary:2f}")


emp1 = Employee("E102","Ayush Mehta",50000)
emp1.calculate_salary()
emp1.display_details()
