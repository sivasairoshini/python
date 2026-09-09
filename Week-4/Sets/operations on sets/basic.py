#Name:T.S.S.Roshini
#Program:To find their union, intersection, difference, and symmetric difference.
s1={1,2,3,44,5}
s2={3,5,6,7}
print("s1:",s1)
print("s2:",s2)
print("s1|s2",s1|s2)
print("s1&s2",s1&s2)
print("s1-s2",s1-s2)
print("s2-s1",s2-s1)
print("s1^s2",s1^s2)
#output
#s1: {1, 2, 3, 5, 44}
#s2: {3, 5, 6, 7}
#s1|s2 {1, 2, 3, 5, 6, 7, 44}
#s1&s2 {3, 5}
#s1-s2 {1, 2, 44}
#s2-s1 {6, 7}
#s1^s2 {1, 2, 6, 7, 44}