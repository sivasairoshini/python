#Name:T.S.S.Roshini
#Program:To Count the occurrences of a specific character in a string.
s=input("Enter the String:").lower()
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
x=input("Enter the character:")
print(f"The no of occurances of a {x} is {d[x]}")
#output
#Enter the String:Problem solving using python
#Enter the character:y
#The no of occurances of a y is 1