#Name:T.S.S.Roshini
#Program:Find all the duplicate characters in a string and their counts.
s=input("Enter the string:").lower()
d={}
for i in s:
    if i not in d:
        d[i]=s.count(i)
for i in d:
    if d[i]>1:
        print(f"{i} occured {d[i]} times")
#output
#Enter the string:Talented
#t occured 2 times
#e occured 2 times