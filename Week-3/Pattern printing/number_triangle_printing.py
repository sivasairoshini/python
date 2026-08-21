#Name:T.S.S.Roshini
#Program:Printing number triangle 
n=int(input("Enter no of rows\n"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(str(i)+" ",end="")
    print()
#output
#Enter no of rows
#5
#1 
#2 2 
#3 3 3 
#4 4 4 4 
#5 5 5 5 5 