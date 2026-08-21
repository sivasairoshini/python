#Name:T.S.S.Roshini
#Program:Printing numbers in between 2 numbers
n,m=map(int,input("Enter the limits\n").split())
for i in range(n,m):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
