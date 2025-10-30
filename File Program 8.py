f1 = open("a.txt",'w+')
inp = input("Enter a line in small case: ")
f1.write(inp)
f1.seek(0)


f2 = open("b.txt",'w+')
data = f1.read()
chars = list(data)
chars2 = []
for i in range(len(chars)):
    chars[i] = chars[i].upper()
    chars2.append(chars[i])
data2 = "".join(chars)
f2.write(data2)


f1.close()
f2.close()
