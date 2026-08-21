#Name:T.S.S.Roshini
#Program:Printing Pyramid
n=int(input('Enter no of levels\n'))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,(2*i)-1):
        print("* ",end="")
    print()
#output
#Enter no of levels
#5
#    * 
#   * * * 
#  * * * * * 
# * * * * * * * 
#* * * * * * * * * 