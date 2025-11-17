class BankAccount:

    def __init__(self,acc_name,acc_num,balance):
        self.acc_name = acc_name
        self.acc_num = acc_num
        self.balance = balance


    '''def accept(self):
        print("\nInput the Bank Account Holder Details: ")
        self.acc_name = input("Acc Holder Name = ")
        self.acc_num = int(input("Acc Number = "))
        self.balance = int(input("Balance = "))'''


    def display(self):
        print("\nBank Account Holder Details: ")
        print("Acc Name = ",self.acc_name)
        print("Acc Num = ",self.acc_num)
        print("Balance = ",self.balance)


    def deposit(self):
        print("\nEnter Deposit Details: ")
        amt_d = int(input("Deposit Amount = "))
        self.balance+= amt_d
        print("Deposit Successful.")
        print("New Balance = ",self.balance)


    def withdraw(self):
        print("\nEnter Withdrawal Details: ")
        amt_w = int(input("Withdrawal Amount = "))
        if(self.balance>=amt_w):
            self.balance-= amt_w
            print("Withdrawal Successful.")
            print("New Balance = ",self.balance)
        else:
            print("Insufficient Balance")


a1 = BankAccount('Harsha',2006,5678)
a1.display()
a1.deposit()
a1.withdraw()
