# input set of strings and display in sorted order as per length

import sys
strings = []
for i in sys.argv[1:]:
    strings.append(i)

print("Original Array: ",strings)

l = len(strings)
for i in range (0,l,1):
    for j in range (0,l,1):
        l1 = len(strings[i])
        l2 = len(strings[j])
        if(l1<l2):
            temp = strings[i]
            strings[i] = strings[j]
            strings[j] = temp

print("Sorted Array: ",strings)
