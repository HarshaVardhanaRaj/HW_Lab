f1 = open("a.txt", "w+")
print("Enter multiple lines with line number (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":   # stop when user just presses Enter
        break
    lines.append(line)
text = "\n".join(lines) # Join all lines with newline characters
f1.write(text)
f1.seek(0)


lines = f1.readlines()
l = len(lines)

f2 = open("b.txt", "w+")
data = []
for i in range(l):
    l2 = len(lines[i])
    data.append(lines[i][1:l2])
f2.write(data)
f3.seek(0)
