users = ['Tyson','Harsha','Andrew','Bill','Camic']
pan_nos = ['A1KD73J','KP68DUW','K9AJD6S','A28FHA6','GD39D7N']
age = ['19','18','25','32','26']
address = ['Bangalore','Chennai','Coimbatore','Delhi','Mumbai']

user_name = input("Enter your Name: ")
pan_num = input("Enter your PAN No.: ")

x = users.index(user_name)
y = pan_nos.index(pan_num)

if(x==y):
    print("Your Details are:")
    print("\tName\t: ",users[x])
    print("\tPAN No.\t: ",pan_nos[x])
    print("\tAge\t: ",age[x])
    print("\tAddress\t: ",address[x])
else:
    print("Name or PAN no. mismatch. Try again.")
