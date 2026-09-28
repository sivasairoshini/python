#Name:T.S.S.Roshini
#Program:GCD Using Recursion (Euclidean Algorithm)
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a,b=map(int,input("Enter a and b values:").split())
print("Result:",gcd(a,b))
#output
#Enter a and b values:18 48
#Result: 6