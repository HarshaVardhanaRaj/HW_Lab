#numpy problem 1

from datetime import datetime

now = datetime.now()

print("\nCurrent Date and Time =",now)

birth_year = int(input("\nEnter your birth year: "))

current_year = now.year
age = current_year - birth_year

print(f"\nYou are {age} years old.")
