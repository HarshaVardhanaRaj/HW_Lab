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


word = input("Enter a word: ")

print("Last occurence of the word in the file:")

content = f1.read()

last_index = content.rfind(word)

print(last_index)
