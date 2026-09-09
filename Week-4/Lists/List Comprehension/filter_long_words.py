#Name:T.S.S.Roshini
#Program:Using list comprehension to create anew list containing words with more than four letters
list1=["roshi","cat","rabbit","rohit sharma","virat","gill"]
list2=[x for x in list1 if len(x)>4]
print("Elements whose length is greater than 4:",list2)
#output
#Elements whose length is greater than 4: ['roshi', 'rabbit', 'rohit sharma', 'virat']