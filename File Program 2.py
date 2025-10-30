f1 = open("a.txt", "w")
text = input("Enter file 1 content: ")
f1.write(text)
f1.close()

with open("a.txt", "r") as f1:
    data = f1.read()

with open("b.txt", "w+") as f2:
    f2.write(data)
    f2.seek(0) #brings the pointer back to starting point
    copy = f2.read()


    print("File 1 contents are copied to File 2")
    print("File 2 contents = ",copy)

