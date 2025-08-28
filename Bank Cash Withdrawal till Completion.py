import sys
bal = float(input("Enter you acc balance: "))
while(bal>=0):
    w_amt = float(input("Enter amount required: "))
    if(w_amt<=bal):
        bal = bal-w_amt
        print("Withdrawal of Rs.",w_amt,"Successful.")
        if(bal==0):
            sys.exit(0)
    else:
        print("Insufficient Balance = ",bal)
