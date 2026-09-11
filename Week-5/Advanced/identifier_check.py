#Name:T.S.S.Roshini
#Program:To Write a program to check if a string is a valid identifier (like a Python variable name).
import keyword
s=input("Enter the identifier:").lower()
if s.isidentifier() and not(keyword.iskeyword(s)):
    print("valid Identifier")
else:
    print("Invalid Identifier")
#output
#Enter the identifier:while
#Invalid Identifier