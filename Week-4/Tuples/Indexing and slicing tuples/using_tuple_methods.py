#Name:T.S.S.Roshini
#Program:To find the maximum and minimum values in a tuple of numbers, and count how many times a given value occurs using the count() method.
t=(1,2,5,7,6,4,3,9,8,57,64,34,38,57,64,57,3,3,33,44,45,45,45,45)
print("Maximum value is:",max(t))
print("Minimum value is:",min(t))
d={}
for x in t:
    if x not in d:
        d[x]=t.count(x)
for x,y in d.items():
    print(f"Count of {x} is {y}")
#output
#Maximum value is: 64
#Minimum value is: 1
#Count of 1 is 1
#Count of 2 is 1
#Count of 5 is 1
#Count of 7 is 1
#Count of 6 is 1
#Count of 4 is 1
#Count of 3 is 3
#Count of 9 is 1
#Count of 8 is 1
#Count of 57 is 3
#Count of 64 is 2
#Count of 34 is 1
#Count of 38 is 1
#Count of 33 is 1
#Count of 44 is 1
#Count of 45 is 4