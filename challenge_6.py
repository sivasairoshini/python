#Name: T.S.S.Roshini
#Lab:06
#Task:challenge
#Program:star pattern
n=int(input("enter no of levels of triangle"))
for i in range(0,n):
    if(i>=0):
        for j in range(0,i+1):
            print("* ",end="")
    print()