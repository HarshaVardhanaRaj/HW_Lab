print("Enter a line: ")
line = input()
l = len(line)
if(line[l-1]!=' '):
    line = line+' '


words = [] ; word = ""
for ch in line:
    if(ch!=' '):
        word+=ch
    else:
        words.append(word)
        word=""
print(words)
