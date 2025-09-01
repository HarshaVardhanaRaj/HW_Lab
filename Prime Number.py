num = int(input("Enter a number: "))
i = 1 ; c = 0
while(i<=num):
    if(num%i==0):
        c+=1
    i+=1
if(c==2):
    print("Prime.")
else:
    print("Not Prime.")
