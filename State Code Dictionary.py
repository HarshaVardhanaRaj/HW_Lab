import sys
state_code = {"TN":1 , "KL":2 , "KA":3, "AP":4, "GA":5, "DL":6, "MH":7}
print("Enter the State name, and get its Code. Enter 0 to exit.")
while(True):
    s = input("State/Choice: ")
    if s in state_code:
        print("State = ",s,"\tCode= ",state_code[s])
    elif s=='0':
        print("Process Terminated.")
        sys.exit(0)
    else:
        print("State not found. Do you wish to add it?")
        c = input("Choice (Y/N): ")
        if c=='Y':
            code = int(input("Enter the code for it: "))
            state_code[s] = code
        else:
            continue
