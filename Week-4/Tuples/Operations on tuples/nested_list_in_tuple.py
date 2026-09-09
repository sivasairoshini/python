#Name:T.S.S.Roshini
#Program:Given a tuple containing a nested list, modify the nested list and explain (in a comment) why this is possible despite tuples being immutable.
t=("Ravi",[1,2,3,4,[4,5]],"Ram","Sai")
print('Initial tuple',t)
l=t[1]
l.append(5)
print("After appending:",t)
#its possible to append because list is mutable and we're not changing the element in tuple we're just changing the elements in the list
#output
#Initial tuple ('Ravi', [1, 2, 3, 4, [4, 5]], 'Ram', 'Sai')
#After appending: ('Ravi', [1, 2, 3, 4, [4, 5], 5], 'Ram', 'Sai')