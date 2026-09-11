#Name:T.S.S.Roshini
#Program:Check if two strings are anagrams of each other.
s1=input("Enter 1st string:")
s2=input("Enter 2nd string:")
d1={};d2={}
for i in s1:
    if i not in d1:
        d1[i]=s1.count(i)
for i in s2:
    if i not in d2:
        d2[i]=s2.count(i)
if d1==d2:
    print("Both strings are Anagrams")
else:
    print("Strings are not Anagrams")
#output
#Enter 1st string:listen
#Enter 2nd string:silent
#Both strings are Anagrams