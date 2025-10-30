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
t=0 ; v=0
vowels = ['a','e','i','o','u']

for i in data:
    if(i.isalpha()):
        t+=1
    if(i in vowels):
        v+=1
c = t-v
print("No. of vowels = ",v)
print("No. of consonants = ",c)

