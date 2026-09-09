#Name:T.S.S.Roshini
#Program:Palindrome checking
n=int(input("Enter the number\n"))
x=n;rev=0
while x!=0:
    y=x%10
    x=x//10
    rev=rev*10+y
if rev==n:
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is not a Paliondrome number")
#output
#Enter the number
#999
#999 is not a Paliondrome number