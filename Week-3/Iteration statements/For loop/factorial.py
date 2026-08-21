#Name:T.S.S.Roshini
#Program:Factorial of a number
n=int(input("Enter the number\n"))
f=1
for i in range(1,n+1):
    f=f*i
    i+=1
print(f"Factorial of {n} is {f}")
#output
#Enter the number
#5
#Factorial of 5 is 120