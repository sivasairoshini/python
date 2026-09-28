#Name:T.S.S.Roshini
#Program:Power Function Using Recursion
def power(base, exp):
    if exp==0:
        return 1
    elif exp<0:
        return 1/power(base,-exp)
    else:
        return base*power(base,exp-1)
base=int(input("Enter the base:"))
exp=int(input("Enter the exponent:"))
print("Result:",power(base,exp))
#output
#Enter the base:5
#Enter the exponent:2
#Result: 25