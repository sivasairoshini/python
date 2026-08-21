#Name:T.S.S.Roshini
#Program:Printing Pascal's-Triangle-style pattern using increasing then decreasing numbers
n=int(input("Enter number of levels\n"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(str(j)+" ", end="")
    for k in range(i - 1, 0, -1):
        print(str(k)+" ", end="")
    print()
#output
#Enter number of levels
#5
#1 
#1 2 1 
#1 2 3 2 1 
#1 2 3 4 3 2 1 
#1 2 3 4 5 4 3 2 1 