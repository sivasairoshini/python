#Name:T.S.S.Roshini
#Program:Nested Functions and the nonlocal Keyword
def make_counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        print(count)
    return increment
counter=make_counter()
counter()
counter()
counter()
counter()
counter()
#output****
#1
#2
#3
#4
#5