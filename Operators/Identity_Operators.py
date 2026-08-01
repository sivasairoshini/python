#Name: T.S.S.Roshini
#Program:Identity Operators
#Task:B7.1-Identity Operators
list1=[5,7,6,4,4,9]
list2=[5,7,6,4,4,9]
list3=list1
print("list1==list2 is",list1==list2)
print("list1==list3 is",list1==list3)
print('list2==list3 is',list2==list3)
print('list1 is list2 is',list1 is list2)
print('list1 is list3 is',list1 is list3)  
print('list2 is list3 is',list2 is list3)
print("list1 is not list2 is",list1 is not list2)
print("list1 is not list3 is",list1 is not list3)
print('list2 is not list3 is',list2 is not list3)
print("id of list 1 is ",id(list1))
print("id of list 2 is ",id(list2))
print("id of list 3 is ",id(list3))
print("Therefore the above answers are correct because thay all share same memory location or they are mapped to same memory")
#output
#list1==list2 is True
#list1==list3 is True
#list2==list3 is True
#list1 is list2 is False
#list1 is list3 is True
#list2 is list3 is False
#list1 is not list2 is True
#list1 is not list3 is False
#list2 is not list3 is True
#id of list 1 is  4355234112
#id of list 2 is  4355394752
#id of list 3 is  4355234112
#Therefore the above answers are correct because thay all share same memory location or they are mapped to same memory
