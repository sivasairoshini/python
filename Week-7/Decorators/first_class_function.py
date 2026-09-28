#Name:T.S.S.Roshini
#Program:First-Class Function Warm-Up
def greet(name):
    return "Hello " + name
say_hello = greet
print(say_hello("Roshi"))
def square(x):
    return x * x
def operate(func, x):
    return func(x)
print(operate(square, 5))
def create_multiplier():
    def multiply(x):
        return x * 2
    return multiply
double = create_multiplier()
print(double(5))
#output
#Hello Roshi
#25
#10