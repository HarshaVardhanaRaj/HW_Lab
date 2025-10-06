# decimal to binary conversion using function

def dec_to_bin(n):
    b= ''
    while(n>0):
        if(n%2==0):
            b = b + '0'
        else:
            b = b + '1'
        n = n//2
    return(b[::-1])

num = int(input("Enter an integer: "))
print("Binary Eq of",num,"=",dec_to_bin(num))
