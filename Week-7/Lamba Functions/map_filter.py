#Name:T.S.S.Roshini
#Program:Lambda Inside map() and filter()
l=[4, 6, 9, 11, 12, 15, 20, 21]
a=list(map(lambda i:i**3,l))
print("Cubes of elements in list:",a)
l=list(filter(lambda x:x%3==0,l))
print("Numbers divisible by 3 are :",l)
#output
#Cubes of elements in list: [64, 216, 729, 1331, 1728, 3375, 8000,9261]
#Numbers divisible by 3 are : [6, 9, 12, 15, 21]