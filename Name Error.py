#Name Error

'''username = 'Harsh'
print(user)
'''

try:
    username = 'Harsh'
    print(user)
except NameError:
    print("Wrong Variable")
