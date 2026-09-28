#Name:T.S.S.Roshini
#Program:Sorting with Lambda as key
students = [("Priya", 85), ("Kiran", 71), ("Anu", 96), ("Rahul", 63), ("Meena", 89)]
a=sorted(students,key=lambda s:s[1],reverse=True)
print(a)
fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
b=sorted(fruits,key=lambda k:len(k),reverse=True)
print(b)
#output
#[('Anu', 96), ('Meena', 89), ('Priya', 85), ('Kiran', 71), ('Rahul', 63)]
#['Banana', 'Orange', 'Grapes', 'Apple', 'Mango']