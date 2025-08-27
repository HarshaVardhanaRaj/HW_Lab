base_price = float(input("Enter base price of ticket: "))
age = float(input("Enter age in years: "))
if(0.0<=age<=12.0):
    print("Final Ticket Price =",(0.5*base_price))
elif(age>=60):
    print("Final Ticket Price =",(0.7*base_price))
elif(age<0):
    print("Invalid Input")
else:
    print("Final Ticket Price =",(1*base_price))