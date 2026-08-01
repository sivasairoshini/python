#Name: T.S.S.Roshini
#Lab:03
#Task:01
#Program:Variables and Data Types
name="Siva Sai Roshini" 
age=18
height=5.3
is_student=True
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
#ouput
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'bool'>
#Lab:03
#Task:02
#Program:Multiple variable assignment
a,b,c=10,20,30
print("a =",a)
print("b =",b)
print("c =",c)
p=q=r=100
print("p =",p)
print("q =",q)
print("r =",r)
#output
#a = 10
#b = 20
#c = 30
#p = 100
#q = 100
#r = 100
#Lab:03
#Task:03
#Program:Swapping of two variables
#using temp variable
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
temp=a
a=b
b=temp
print("After swapping")
print("a =",a)
print("b =",b)
#Swapping by tuple unpacking
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
a,b=b,a
print("After swapping by tuple unpacking i.e a,b=b,a")
print("a =",a)
print("b =",b)
#output
#Enter 'a'value:15
#Enter 'b' value:20
#After swapping
#a = 20
#b = 15
#Enter 'a'value:64
#Enter 'b' value:57
#After swapping by tuple unpacking i.e a,b=b,a
#a = 57
#b = 64
#Lab:03
#Task:04
#Program:Dynamic typing
balance=1000.5432
print(type(balance))
balance=570
print(type(balance))
#output
#<class 'float'>
#<class 'int'>
#Lab:03
#Task:challenge
#Program:Calaculatng the area and circumfernce of a circle
radius=float(input("Enter the radius\n"))
area=(3.14*radius*radius)
circumference=(2*3.14*radius)
print("Area of circle is",area)
print("Circumference of circle is",circumference)
#output
#Enter the radius
#50
#Area of circle is 7850.0
#Circumference of circle is 314.0