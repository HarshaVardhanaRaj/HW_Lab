light = input("Color of Traffic Light: ")
light = light.lower()   #to prevent case sensitive errors
if(light=='red'):
    print("Stop")
elif(light=='yellow'):
    print('Slow')
elif(light=='green'):
    print("Go")
else:
    print("Invalid Input")