#Name:T.S.S.Roshini
#Program:To iterate through a dictionary and print all keys, all values, and all key-value pairs using keys(), values(), and items().
d={'Roshini': '101', 'Deekshitha': '102', 'Sandhya': '103', 'Neeraja': '104', 'Ram Sai': '105'}
for i in d.keys():
    print(i,end=",")
print()
for j in d.values():
    print(j,end=",")
print()
for x,y in d.items():
    print(f"{x}:{y}")
#output
#Roshini,Deekshitha,Sandhya,Neeraja,Ram Sai,
#101,102,103,104,105,
#Roshini:101
#Deekshitha:102
#Sandhya:103
#Neeraja:104
#Ram Sai:105