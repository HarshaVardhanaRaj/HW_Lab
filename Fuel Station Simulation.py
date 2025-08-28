import sys
fuel = float(input("Enter amount of fuel filled (in L): "))
mileage = float(input("Enter mileage of car (km/L): "))
km_driven = 0
while(km_driven/mileage < fuel):
    km_driven = km_driven + 1
print(km_driven,"kms driven. Tank is empty.")
