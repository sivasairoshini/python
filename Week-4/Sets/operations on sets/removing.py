#Name:T.S.S.Roshini
#Program:To remove an element from a set using remove() and discard(), and explain (in a comment) the difference in behavior when the element does not exist.
s={1,2,3,4,5,6,7}
s.remove(2)
print(s)
s.discard(7)
print(s)
#s.remove(9)
s.discard(9)
print(s.discard(9))
#output
# s.remove(9)
#    ~~~~~~~~^^^
#KeyError: 9
#because remove will give error whenevr we're going delete element which's not in st
#whereas discard will remove if present else it wont return any error
#{1, 3, 4, 5, 6, 7}
#1, 3, 4, 5, 6}
#None