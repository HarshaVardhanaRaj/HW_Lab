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


f2 = open("b.txt", "w+")
print("Enter multiple lines (press Enter on an empty line to finish):")
lines = []
while True:
    line = input()
    if line == "":   # stop when user just presses Enter
        break
    lines.append(line)
text = "\n".join(lines) # Join all lines with newline characters
f2.write(text)
f2.seek(0)

lines1 = f1.readlines()
lines2 = f2.readlines()

#print(lines1)
#print(lines2)

f3 = open("c.txt","w+")
max_len = max(len(lines1), len(lines2))
merged_lines = []
for i in range(max_len):
    if i < len(lines1):
        merged_lines.append(lines1[i].rstrip("\n"))
    if i < len(lines2):
        merged_lines.append(lines2[i].rstrip("\n"))
f3.write("\n".join(merged_lines))
f3.seek(0)

# Read and print merged file
print(f3.read())

# Close all files
f1.close()
f2.close()
f3.close()
