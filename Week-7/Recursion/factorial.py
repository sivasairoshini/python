#Name:T.S.S.Roshini
#Program:Factorial Using Recursion
def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
n=int(input("Enter the number to find factorial\n"))
print("Factorial:",fac(n))
#output
#Enter the number to find factorial
#6
#Factorial: 720