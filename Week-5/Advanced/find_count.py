#Name:T.S.S.Roshini
#Program:To Implement your own version of str.find() and str.count() without using built-in string methods.
s=input("Enter the string:").lower()
found=0;count=0
x=input("Enter the character to find:").lower()
for i in range(len(s)):
    if x==s[i] and found==0:
        found=1
        print(f"{x} is present at index {i}")
        break
if found==0:
    print(f"{x} is not present")
y=input("Enter the character to find its count:").lower()
for i in s:
    if y==i:
        count+=1
print(f"Count of {y} is {count}")
#output
#Enter the string:Everything happens for a reason
#Enter the character to find:e
#e is present at index 0
#Enter the character to find its count:e
#Count of e is 4