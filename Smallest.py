#smallest of 2

import sys
a = sys.argv[1]
b = sys.argv[2]

if(a<b):
    print("Assertion Error.",a,"is smallest.")
else:
    print(b,"is smallest.")
