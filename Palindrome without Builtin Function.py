str = input("Enter a string: ")
rev = ""
for i in range(len(str)-1,-1,-1):
    rev = rev + str[i]
if(rev==str):
    print("Palindrome")
else:
    print("Not Palindrome")
