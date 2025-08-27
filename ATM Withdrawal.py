bal = (float(input("Enter your Balance: ")))
w_amt = (int(input("Enter Withdrawal Amount: ")))
if(w_amt%100==0 and bal>=w_amt and w_amt>=0 and bal>=0):
    print("Withdrawal Allowed.")
elif(w_amt%100==0 and bal<w_amt and w_amt>=0 and bal>=0):
    print("Insufficient Balance.")
elif(w_amt%100!=0 and w_amt>=0 and bal>=0):
    print("Invalid Denomination. Enter Amount in 100s.")
else:
    print("Error. Invalid Input.")