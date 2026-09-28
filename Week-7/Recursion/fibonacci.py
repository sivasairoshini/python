#Name:T.S.S.Roshini
#Program:Fibonacci Series Using Recursion
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the no of terms:"))
for i in range(n):
    print(fibonacci(i),end=" ")
#output
#Enter the no of terms:5
#0 1 1 2 3