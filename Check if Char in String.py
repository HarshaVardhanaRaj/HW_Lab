import sys
str = input("Enter a sentence: ")
ch = input("Enter the character that needs to be found: ")

'''
if (ch in str): #using built-in function
    print(ch,"is present in the sentence at index",str.index(ch))
else:
    print("Not present")
    break
'''

for i in range (0,len(str),1):
    c = str[i]
    if(ch==c):
        print(ch,"is present in the sentence at index",i)
        sys.exit(0)
        
print("Not present")
