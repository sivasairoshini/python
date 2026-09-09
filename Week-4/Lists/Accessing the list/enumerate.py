#Name:T.S.S.Roshini
#Program:Using enumerate() method
list=[]
n=int(input("Enter the no of elements:"))
for i in range(n):
    number=int(input("Enter the number: "))
    list.append(number)
for i, value in enumerate(list):
    print(f"list[{i}]:{value}")
#output
#Enter the no of elements:3
#Enter the number: 1
#Enter the number: 2
#Enter the number: 3
#list[0]:1
#list[1]:2
#list[2]:3