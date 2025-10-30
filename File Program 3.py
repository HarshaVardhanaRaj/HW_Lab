f1 = open("a.txt", "w+")


print("Enter multiple lines (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":   # stop when user just presses Enter
        break
    lines.append(line)

    
text = "\n".join(lines) # Join all lines with newline characters
f1.write(text)
f1.seek(0)


data = f1.read()
c=0
for i in data:
    if(i.isalpha()):
        c+=1
print("No. of characters = ",c)


f1.close()

