#Name:T.S.S.Roshini
#Program:Basic Lambda Functions
a=lambda x:x*x
b=lambda x:"Even" if x%2==0 else "Odd"
c=lambda x,y:x if x>y else y
n=int(input("Enter the number to which you want to find the square:"))
print(f"Square of {n} is {a(n)}")
n=int(input("Enter the number to find even or odd:"))
print(f"{n} is {b(n)}")
a,b=map(int,input("Enter the numbers to find largest").split())
print(f"Largest of {a} and {b} is {c(a,b)}")
#output
#Enter the number to which you want to find the square:5
#Square of 5 is 25
#Enter the number to find even or odd:18
#18 is Even
#Enter the numbers to find largest57 64
#Largest of 57 and 64 is 64