mport sys
while(True):
    s = input("Enter a String or 'QUIT' to exit: ")
    s = s.upper()
    if(s=="QUIT"):
        print("Program Terminated.")
        sys.exit(0)
    else:
        print("Length of String =",len(s))
