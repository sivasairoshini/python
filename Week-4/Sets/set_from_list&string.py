#Name:T.S.S.Roshini
#Program:To create a set from a list and from a string, and print the results.
l=[1,2,3,5,7,6,4]
s="Madam".lower()
s1=set(l)
s2=set(s)
print(f"Original list:{l} and it's set:{s1}")
print(f"Original string:{s} and it's set:{s2}")
#output
#Original list:[1, 2, 3, 5, 7, 6, 4] and it's set:{1, 2, 3, 4, 5, 6, 7}
#Original string:madam and it's set:{'a', 'd', 'm'}