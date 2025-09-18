# Cloning in Python

grocery_list = ["Milk", "Bread", "Eggs"]
shared_list = grocery_list[:]
print(id(grocery_list))
print(id(shared_list))
shared_list.append("Butter")
print(grocery_list)
print(shared_list)
