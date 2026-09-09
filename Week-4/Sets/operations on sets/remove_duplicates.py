#Name:T.S.S.Roshini
#Program:To use a set to print only the unique elements,then convert the result back into a sorted list.
l=[1,2,3,4,7,6,5,6,4,2,4,1,2,8,100,57,34,64,47,64]
s=set(l)
print("Set with unique elements of list:",s)
l2=list(s)
l2.sort()
print("After Sorting and Removing repeated elements the list is :",l2)
#output
#Set with unique elements of list: {64, 1, 2, 3, 4, 5, 6, 7, 8, 100, 34, 47, 57}
#After Sorting and Removing repeated elements the list is : [1, 2, 3, 4, 5, 6, 7, 8, 34, 47, 57, 64, 100]