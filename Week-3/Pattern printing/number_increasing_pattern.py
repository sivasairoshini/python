#Name:T.S.S.Roshini
#Program:Printing a number triangle with increasing sequence
n=int(input("Enter no of rows\n"))
for i in range(1,n+1):
    k=1
    for j in range(1,i+1):
        print(str(k)+" ",end="")
        k=k+1
    print()
#output
#Enter no of rows
#5
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 