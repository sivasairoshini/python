#Name: T.S.S.Roshini
#Program:Fruit Membership Check
#Task:B6.1-Membership Operators
fruits=["kiwi","guava","dragon fruit","avacado"]
fruit1=input("Enter any fruit name\n")
print(f'{fruit1} in fruits ??',fruit1 in fruits)
print(f'{fruit1} not in fruits ??',fruit1 not in fruits)
fruit2=input("Enter any fruit name again\n")
print(f'{fruit2} in fruits ??',fruit2 in fruits)
print(f'{fruit2} not in fruits ??',fruit2 not in fruits)
#output
#Enter any fruit name
#mango
#mango in fruits ?? False
#mango not in fruits ?? True
#Enter any fruit name again
#kiwi
#kiwi in fruits ?? True
#kiwi not in fruits ?? False