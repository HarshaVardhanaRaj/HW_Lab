# Value Error

'''int("abc")

a,b = [1,2,3]
'''

try:
    print(int("abc"))
except ValueError:
    print("Wrong Input")


try:
    n = int(input("Num = "))
    print(a**2)
except (KeyboardInterrupt, NameError):
    print("Recheck Variable Name")
