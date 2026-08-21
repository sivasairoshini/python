#Name:T.S.S.Roshini
#Program:Checking wheather the given triangle form a triangle and then determining the the type of triangle
a,b,c=map(int,input("Enter the sides of the triangle\n").split())
if a<b+c or b<a+c or c<a+b :
    if a==b and b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or a==c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Cannot form Triangle")
#output
#Enter the sides of the triangle
#3 4 5
#Scalene Triangle
