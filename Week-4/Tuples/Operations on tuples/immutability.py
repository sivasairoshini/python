#Name:T.S.S.Roshini
#Program:Demonstrates tuple immutability by attempting to modify an element and catching the resulting error using try/except.
t=(1,2,3,4)
t.append(5)
print(t)
#output
#t.append(5)
#    ^^^^^^^^
#AttributeError: 'tuple' object has no attribute 'append'