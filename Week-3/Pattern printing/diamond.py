#Name:T.S.S.Roshini
#Program:Printing Diamond shaped pattern
n=int(input("Enter no of levels"))
for i in range(1, n + 1):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("* ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("* ", end="")
    print()
#output
#Enter no of levels5
#    * 
#   * * * 
#  * * * * * 
# * * * * * * * 
#* * * * * * * * * 
# * * * * * * * 
#  * * * * * 
#   * * * 
#    * 