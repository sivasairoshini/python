#Name:T.S.S.Roshini
#Program:Checking the number is prime or not
n=int(input("Enter the number\n"))
f=0
for i in range(2,n):
    if n%i==0:
        f=1
        break
if(f==0):
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")
#output
#Enter the number
#7
#7 is prime number