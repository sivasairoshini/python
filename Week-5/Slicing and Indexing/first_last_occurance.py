#Name:T.S.S.Roshini
#Program:Find the index of the first and last occurrence of a character.
s=input("Enter the string:").lower()
x=input("Enter the character").lower()
l=[]
for i in range(len(s)):
    if s[i]==x:
        l.append(i)
if len(l)==0:
    print("No such character")
elif len(l)==1:
    print("only once at 0")
else:
    print("First occurance:",l[0])
    print("Last occurance:",l[-1])
#output
#Enter the string:Connected
#Enter the characterc
#First occurance: 0
#Last occurance: 5