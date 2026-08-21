#Name:T.S.S.Roshini
#Program:Printing Right angled triangle pattern
n=int(input("Enter no of levels\n"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()
#output
#Enter no of levels
#5
#* 
#* * 
#* * * 
#* * * * 
#* * * * * 