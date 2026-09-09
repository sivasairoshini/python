#Name:T.S.S.Roshini
#Program:List slicing
list=[]
for i in range(10):
    n=int(input())
    list.append(n)
print("List upto 3 elements:",list[0:3])
print("Last 3 elements:",list[-3:])
print("Alternate elements:",list[::2])
#output
#2
#3  
#4
#5
#6
#7
#8
#9
#10
#11
#List upto 3 elements: [2, 3, 4]
#Last 3 elements: [9, 10, 11]
#Alternate elements: [2, 4, 6, 8, 10]