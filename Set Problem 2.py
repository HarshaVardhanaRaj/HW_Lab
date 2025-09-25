prime_numbers = {2,3,5,7,11}
fibonacci_set = {0,1,1,2,3,5,8,13,21,34}

c = prime_numbers|fibonacci_set
print("Union =",c)

d = prime_numbers&fibonacci_set
print("Intersection =",d)

x = prime_numbers.difference(fibonacci_set)
print("Difference =",x)

y = prime_numbers.symmetric_difference(fibonacci_set)
print("Symmetric Difference =",y)
