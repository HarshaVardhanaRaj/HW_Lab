import sys
import random
num = random.randint(1,100)
while(True):
    n = int(input("Guess the number from 1 to 100: "))
    if(n==num):
        print("Congratulations! Correct guess.")
        sys.exit(0)
    elif(n>num):
        print("Wrong. Guess lower.")
    else:
        print("Wrong. Guess higher.")