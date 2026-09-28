#Name:T.S.S.Roshini
#Program:Using reduce() to Aggregate Data
from functools import reduce
numbers = [2, 3, 4, 5]
result = reduce(lambda a, b: a * b, numbers)
print(result)
#output
#120
from functools import reduce
words = ["Python", "is", "very", "interesting"]
result = reduce(lambda a, b: a + " " + b, words)
print(result)
#output
#Python is very interesting
from functools import reduce
numbers = [12, 45, 23, 67, 34, 89, 10]
result = reduce(lambda a, b: a if a > b else b, numbers)
print(result)
#output
#89