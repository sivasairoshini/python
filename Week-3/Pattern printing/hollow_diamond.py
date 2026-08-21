#Name:T.S.S.Roshini
#Program:Printing a hollow diamond pattern of stars
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
#output
#Enter n: 5
#    *
#   * *
#  *   *
# *     *
#*       *
# *     *
#  *   *
#   * *
#    *