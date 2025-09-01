num = int(input("Enter a number: "))
og = num ; rev = 0 ; num=abs(num)
while(num>0):
    d = num % 10
    rev = rev*10 + d
    num = num // 10
if(og>=0):
    print(og,"reversed =",rev)
else:
    print(og,"reversed =",(-rev))
