#Name:T.S.S.Roshini
#Program:Removing duplicates without using set() function
list=[1,1,1,2,2,3,5,7,57,57,64]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("Original list:",list)
print("List after removing duplicates:",new_list)
#output
#Original list: [1, 1, 1, 2, 2, 3, 5, 7, 57, 57, 64]
#List after removing duplicates: [1, 2, 3, 5, 7, 57, 64]