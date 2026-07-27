#Name: T.S.S.Roshini
#Lab:06
#Task:01
#Program:Indentation and comments
number=int(input("enter the number"))
#if n%2==0:
#print("even number")
#else:
#    print("odd number")
#print("even number")
#   ^
#IndentationError: expected an indented block
if number%2==0:
    print("even number")
else:
    print("odd number")
#output
#enter the number5
#odd number
#Lab:06
#Task:02
#Program:FOR AND IF
for i in range(1,11):
    if(i%2==0):
        print(i,"is even number")
    else:
        print(i,"is odd number")
#output
#1 is odd number
#2 is even number
#3 is odd number
#4 is even number
#5 is odd number
#6 is even number
#7 is odd number
#8 is even number
#9 is odd number
#10 is even number
#Lab:06
#Task:03
#Program:Writing correct code
x=int(input("enter a number"))
if x>0:
    print("positive number")
else:
    print("non positive number")
#output
#enter a number25
#positive number
#Lab:06
#Task:challenge
#Program:star pattern
n=int(input("enter no of levels of triangle"))
for i in range(0,n):
    if(i>=0):
        for j in range(0,i+1):
            print("* ",end="")
    print()
#output
#enter no of levels of triangle5
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 