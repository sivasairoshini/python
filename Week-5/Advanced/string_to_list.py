#Name:T.S.S.Roshini
#Program:Convert a string into a list of characters and back into a string.
s=input("Enter the string:")
l=[i for i in s]
print("List consisteing of characters of string",l)
s1="".join(l)
print(s1)
#output
#Enter the string:Mango
#List consisteing of characters of string ['M', 'a', 'n', 'g', 'o']
#Mango