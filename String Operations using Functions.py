def chars(s):
    c = 0
    for i in s:
        c+=1
    return c

def vowels(s):
    v = 0 ; vowels = ['a','e','i','o','u']
    for i in s:
        if i in vowels:
            v+=1
    return v


def spaces(s):
    sp = 0
    for i in s:
        if (i==' '):
            sp+=1
    return sp


str = input("Enter a String: ")

num_c = chars(str)
num_v = vowels(str)
num_s = spaces(str)

print("No. of chars = ",num_c)
print("No. of vowels = ",num_v)
print("No. of spaces = ",num_s)
