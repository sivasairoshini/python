#Name:T.S.S.Roshini
#Program:Swap the case of each character in a string (upper → lower and vice versa).
s=input("Enter the string:")
result=""
for i in s:
    if i.isalpha():
        if i.islower():
            result+=i.upper()
        else:
            result+=i.lower()
print(result)
#using swapcase
s1=s.swapcase()
print("Using swap case:",s1)
#output
#Enter the string:Rohit Sharma
#rOHITsHARMA
#Using swap case: rOHIT sHARMA