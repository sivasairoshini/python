#Name:T.S.S.Roshini
#Program:Checking largest of three numbers
n1,n2,n3=map(int,input("Enter the numbers\n").split())
if n1>n2 and n1>n3:
    print(f"{n1} is greater")
else:
    if n2>n3:
        print(f"{n2} is greater")
    else:
        print(f"{n3} is greater")
#output
#Enter the numbers
#3 65 13
#65 is greater