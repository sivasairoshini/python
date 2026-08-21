#Name:T.S.S.Roshini
#Program:Reversing a integer
n=int(input("Enter the number\n"))
x=n;rev=0
while x!=0:
    y=x%10
    x=x//10
    rev=rev*10+y
print(f"{rev} is the reverse of {n}")
#output
#Enter the number
#251108
#801152 is the reverse of 251108