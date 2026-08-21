#Name:T.S.S.Roshini
#Program:Generating Fibonacci series
n=int(input("Enter n value\n"))
print("Fibonacci Series")
print("0 1 ",end="")
i=2
a=0
b=1
while i<=n:
    c=a+b
    a=b
    b=c
    i+=1
    print(str(c)+" ",end="")
#output
#Enter n value
#5
#Fibonacci Series
#0 1 1 2 3 5 