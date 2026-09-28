#Name:T.S.S.Roshini
#Program:Stacking Multiple Decorators
import time
from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper
@log_call
@timer
def add(a, b):
    return a + b
print(add(10, 20))
#output
#alling add args=(10, 20) kwargs={}
#add took 0.000000 seconds
#add returned 30
#30