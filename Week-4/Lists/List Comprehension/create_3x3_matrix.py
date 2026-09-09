#Name:T.S.S.Roshini
#Program:Using nested list comprehension to create a 3x3 matrix containing numbers 1 to 9
list=[[(i+j*3)+1 for i in range(3)] for j in range (3)]
print("3x3 matrix:")
for x in list:
    print(x)
#output
#3x3 matrix:
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]