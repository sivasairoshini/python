#Name:T.S.S.Roshini
#Program:To create a set of squares of all odd numbers from 1 to 20.
s={i**2 for i in range(1,21) if i%2!=0}
print(s)
#output
#{1, 121, 225, 289, 9, 169, 361, 81, 49, 25}