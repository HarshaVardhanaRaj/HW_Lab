num = int(input("Enter a number: "))
ang = 0 ; og = num
while(num>0):
    d = num%10
    ang = ang + d*d*d
    num = num // 10
if(ang==og):
    print(og,"is an Armstrong Number.")
else:
    print(og,"is not an Armstrong Number.")
