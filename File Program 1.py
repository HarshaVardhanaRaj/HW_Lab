# File Access Modes

f1 = open("a.txt",'w')
print(f1.mode)

open("b.txt",'w')           #important step
f2 = open("b.txt",'r')
print(f2.mode)


f3 = open("c.txt",'a')
print(f3.mode)

f4 = open("d.txt",'w+')
print(f4.mode)
