#Name:T.S.S.Roshini
#Program:Access-Control Decorator
from functools import wraps
is_logged_in = False
def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in.")
    return wrapper
@require_login
def dashboard():
    print("Welcome to the dashboard!")
print("When is_logged_in = False:")
dashboard()
is_logged_in = True
print("\nWhen is_logged_in = True:")
dashboard()
#output
#When is_logged_in = False:
#Access denied. Please log in.
#
#When is_logged_in = True:
#Welcome to the dashboard!