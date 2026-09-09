#Name:T.S.S.Roshini
#Program:Maximum,Minimum,Sum without inbuilt functions
list=[15,5,8,30,11,25,1,5,26]
min=list[0]
max=list[0]
sum=0
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i
    sum=sum+int(i)
print(f"Minimum of list is {min}")
print(f"Maximum of list is {max}")
print(f"Sum of elements in list is {sum}")
#output
#Minimum of list is 1
#Maximum of list is 30
#Sum of elements in list is 126