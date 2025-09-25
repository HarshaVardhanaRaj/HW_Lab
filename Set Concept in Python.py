# Set Concept in Python

a = {1,2,3,4,5,"c"}
print(a)

b = {"a","b","c", "d", "e",3}
print(b)

c = a|b
print(c)

d = a&b
print(d)

a.remove(5)
print(a)

b.discard("b")
print(b)

#a.remove(6)
#print(a)............. gives an error

b.discard("f")

print(b) #............ no error

x = a.difference(b)
print(x)

y = a.symmetric_difference(b)
print(y)

i = {1,2,3,4,5}
j = {1,2,3}
k = {4,5,6}

print(j.issubset(i))
print(k.issubset(i))
print(i.issuperset(j))
