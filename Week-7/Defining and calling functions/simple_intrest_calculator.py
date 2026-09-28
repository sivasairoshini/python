#Name:T.S.S.Roshini
#Program:Simple Interest Calculator
def simple_interest(principal, rate, time):
    SI=(principal*rate*time)/100
    print(f"{SI} is the simple intrest")
p,r,t=map(int,input("Enter Principle,Rate,Time\n").split())
simple_interest(p,r,t)
#output
#Enter Principle,Rate,Time
#10000 5 2
#1000.0 is the simple intrest