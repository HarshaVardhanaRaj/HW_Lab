a = input("Enter a word/number: ")
rev = "" ; l=len(a); i=l-1
while(i>=0):
    rev = rev + a[i]
    i-=1
print(rev)
if(rev==a):
    print("Palindrome.")
else:
    print("Not Palindrome.")
