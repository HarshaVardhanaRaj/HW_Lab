# binary to decimal convertor

def bin_to_dec(n):
    d=0 ; ns = str(num) ; l = len(ns) ; nsr = ns[::-1]
    for i in range(0,l,1):
        if(nsr[i]=='1'):
            d = d + (2**i)
    return(d)

num = int(input("Enter a Binary Num: "))
print("Decimal Eq of",num,"=",bin_to_dec(num))
