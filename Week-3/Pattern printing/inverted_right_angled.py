#Name:T.S.S.Roshini
#Program:Printing Inverted right angled triangle pattern
n=int(input("Enter the number of levels\n"))
i=n
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print()
#output
#Enter the number of levels
#5
#* * * * * 
#* * * * 
#* * * 
#* * 
#* 