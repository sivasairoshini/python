#Name:T.S.S.Roshini
#Program:To Reverse a given string (without using slicing, then with slicing).
string=input("Enter the String:")
rev1=""
for i in string:
    rev1=i+rev1
print("Reversed string without slicing:",rev1)
rev2=string[::-1]
print("Reversed string with slicing",rev2)
#output
#Enter the String:Java
#Reversed string without slicing: avaJ
#Reversed string with slicing avaJ