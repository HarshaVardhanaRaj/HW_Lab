words = []
print("Enter words to add, or enter 'QUIT' to stop adding: ")

while(True):
    w = input("Input: ")
    if(w=='QUIT'):
        print("List is completed")
        break
    else:
        words.append(w)

longest = ""
for i in words:
    if (len(i)>len(longest)):
        longest = i

print("Longest word = ",longest)
