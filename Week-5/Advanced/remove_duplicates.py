#Name:T.S.S.Roshini
#Program:Remove duplicate characters from a string.
s=input("Enter the string:")
result=""
for i in s:
    if i not in result:
        result=result+i
print(f"{s} after removing duplicates:{result}")
#output
#Enter the string:GLOBAL
#GLOBAL after removing duplicates:GLOBA