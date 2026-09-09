#Name:T.S.S.Roshini
#Program:Converting lists into tuples and tuples into lists
list1=[1,43,57,5,8,11,25,5,26]
tuple1=("Ramya","Dinesh","Manasa")
t=tuple(list1)
l=list(tuple1)
print("Intial list:",list1)
print("List after converting into tuple:",t)
print("Initial tuple:",tuple1)
print("Tuple after converting into list:",l)
#output
#Intial list: [1, 43, 57, 5, 8, 11, 25, 5, 26]
#List after converting into tuple: (1, 43, 57, 5, 8, 11, 25, 5, 26)
#Initial tuple: ('Ramya', 'Dinesh', 'Manasa')
#Tuple after converting into list: ['Ramya', 'Dinesh', 'Manasa']
ch="pwwkew"
current=[]
for x in ch:
    if x not in current:
        current.append(x)
    else:
        continue
print(len(current))