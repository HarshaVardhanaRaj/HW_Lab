a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
choice = int(input("Enter 1 to Add, 2 to Subtract, 3 to multiply, or 4 to divide: "))
match(choice):
    case 1:
        print(a,'+',b,'=',(a+b))
    case 2:
        print(a,'-',b,'=',(a-b))
    case 3:
        print(a,'x',b,'=',(a*b))
    case 4:
        print(a,'/',b,'=',(a/b))
    case _:
        print("Invalid Option")
        
