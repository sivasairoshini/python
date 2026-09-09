#Name:T.S.S.Roshini
#Program:Using list comprehension with a conditional expression to replace negative numbers with zero
list=[-57,64,45,7,-33,-96,-47,43,34,-38]
list1=[0 if i<0 else i for i in list]
print("Elements list after replacing negative numbers with zero:",list1)
#output
#Elements list after replacing negative numbers with zero: [0, 64, 45, 7, 0, 0, 0, 43, 34, 0]