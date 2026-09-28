#Name:T.S.S.Roshini
#Program:Using map() to Transform Data
def celsius_to_fahrenheit(c):
    return (9 / 5) * c + 32
temperatures = [0, 25, 30, 40, 100]
result = list(map(celsius_to_fahrenheit, temperatures))
print(result)
#output
#[32.0, 77.0, 86.0, 104.0, 212.0]
words = ["apple", "banana", "mango", "orange"]
result = list(map(str.upper, words))
print(result)
#output
#['APPLE', 'BANANA', 'MANGO', 'ORANGE']