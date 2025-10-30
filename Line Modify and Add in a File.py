line = input("Enter a sentence with .'s and numbers: ")
chars = list(line)
l = len(chars) ; i=0
while i<l:
    ch = chars[i]
    if ch == '.':
        if i + 2 < l and chars[i + 1] == ' ':
            chars[i + 2] = chars[i + 2].upper()
        elif i + 1 < l:
            chars[i + 1] = chars[i + 1].upper()
    elif(ch.isnumeric()):
        chars.insert(i,"(")
        chars.insert(i+2,")")
        i+=2
        l+=2
    i+=1
line2 = "".join(chars)

f1 = open("a.txt",'w+')
f1.write(line2)
f1.read()
f1.close()
