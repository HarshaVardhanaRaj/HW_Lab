books = 0
books_name = ['']*5
for i in range(0,5):
    books_name[i] = input("Enter Book Name to Borrow: ")
    books+=1
print("5 Books:",books_name,"already borrowed. Can't borrow more.")