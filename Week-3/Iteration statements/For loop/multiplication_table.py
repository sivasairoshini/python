#Name:T.S.S.Roshini
#Program:Multiplication Table 
n=int(input("Enter the number\n"))
print(f"{n} table")
for i in range(1,11):
    x=n*i
    print(f"{n}*{i}={x}")
    i+=1
#output
#Enter the number
#5
#5 table
#5*1=5
#5*2=10
#5*3=15
#5*4=20
#5*5=25
#5*6=30
#5*7=35
#5*8=40
#5*9=45
#5*10=50