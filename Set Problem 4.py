dict1 = {6:'Ether'  ,2:'Bitcoin'    ,1:'Gas'    ,9:'Litecoin'   ,7:'Ganache'    ,8:'Ethereum'}
print(dict1)
#print(dict1[1])
for i in range(1,10):
    if(i in dict1):
        print(dict1[i])
