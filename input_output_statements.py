#Name: T.S.S.Roshini
#Lab:05
#Task:01
#Program:Next Year's Age Calculator
name=input("Whats your name??")
age=input("Whats your age ??")
print("Hello",name,", you will turn",int(age)+1,"next year")
#output
#Whats your name??Roshini
#Whats your age ??18
#Hello Roshini , you will turn 19 next year
#Lab:05
#Task:02
#Program:Converting strings into numbers and performing arithmetic operations
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print("Sum:",n1+n2)
print("Subtraction:",n1-n2)
print("Product:",n1*n2)
print("Division:",n1//n2)
#output
#Enter first number:57
#Enter second number:64
#Sum: 121
#Subtraction: -7
#Product: 3648
#Division: 0
#Lab:05
#Task:03
#Program:Output Formatting Methods
name="Ram Sai" 
age=18
#Comma separate
print("Name:",name,",Age:",age)
#str.format()
print("Name :{} ,Age : {}".format(name,age))
#f-string
print(f"Name:{name}, Age:{age}")
#output
#Name: Ram Sai ,Age: 18
#Name :Ram Sai ,Age : 18
#Name:Ram Sai, Age:18
#Lab:05
#Task:04
#Program:Taking various inputs using single input function
n1,n2,n3=map(int,input("Enter three numbers:").split())
print("Sum of three numbers is:",n1+n2+n3)
#output
#Enter three numbers:5 4 5
#Sum of three numbers is: 14
#Lab:05
#Task:challenge
#Program:average marks rounded to 2 decimals
m1,m2,m3=map(int,input("enter the marks of 3 subjects").split())
average=(m1+m2+m3)/3
print(f"average marks are{average:.2f}")
#enter the marks of 3 subjects98 100 99
#average marks are99.00