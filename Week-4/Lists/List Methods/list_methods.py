#Name:T.S.S.Roshini
#Program:To demonstrate list methods
list=[1,2]
print("List initially:",list)
list.append(3)
print("List after appending:",list)
list.insert(1,57)
print("List after inserting:",list)
list.extend([64,96,45])
print("List after extending:",list)
result=list.pop()
print(f"list after pop is {list} and the removed element is {result}")
list.append(1)
print(f"Count of element 1 is{list.count(1)}")
print(f" List after removal of element '1' is {list.remove(1)} ")
print(f"Index of element 57 is {list.index(57)}")
list.sort()
print("Sorted list is:",list)
list.reverse()
print("Reversed list is",list)
print(f"List popping based on index is {list.pop(5)} nad the list is{list}")
#output
#List initially: [1, 2]
#List after appending: [1, 2, 3]
#List after inserting: [1, 57, 2, 3]
#List after extending: [1, 57, 2, 3, 64, 96, 45]
#list after pop is [1, 57, 2, 3, 64, 96] and the removed element is 45
#Count of element 1 is2
#List after removal of element '1' is None 
#Index of element 57 is 0
#Sorted list is: [1, 2, 3, 57, 64, 96]
#Reversed list is [96, 64, 57, 3, 2, 1]
#List popping based on index is 1 nad the list is[96, 64, 57, 3, 2]