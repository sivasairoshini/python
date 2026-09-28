#Name:T.S.S.Roshini
#Program: Decorator with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet():
    print("Hello! Welcome!")
greet()
#output
#Hello! Welcome!
#Hello! Welcome!
#Hello! Welcome!