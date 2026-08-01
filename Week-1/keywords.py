#Name: T.S.S.Roshini
#Lab:02
#Task:01
#Program:Python keywords list
import keyword
print(keyword.kwlist)
print("Total number of keywords:",len(keyword.kwlist))
print("Soft keywors:",keyword.softkwlist)
print("Total no of Soft Keywords:",len(keyword.softkwlist))
#ouput
#['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#Total number of keywords: 36
#Soft keywors: []
#Lab:02
#Task:02
#Program:Python keyword checker
import keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("False"))
print(keyword.iskeyword("async"))
print(keyword.iskeyword("name"))
print(keyword.iskeyword("student"))
print(keyword.iskeyword("def"))
print(keyword.iskeyword("or"))
#output
#True
#True
#True
#False
#False
#True
#True
#Lab:02
#Task:Challenge
#Program:printing soft keywords
import keyword
print(keyword.softkwlist)
print(len(keyword.softkwlist))
#output
#[]
#0
