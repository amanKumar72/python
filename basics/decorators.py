# decorators => function returns function with extra functionality 
# @syntax sugar
# function above is just like normal function
# we can call it like that

from functools import wraps

# example 1: logging decorator
def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala")

# example 2 : authentication decorator
from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user")
acess_tea_inventory("admin")

# This function will be tested automatically.
# Do not change the function name or parameters.
from functools import wraps
def cache_results(func):
    # Write your code below this line
    cache = dict()
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        print(key)
        if key in cache:
            return cache[key]
        res = func(*args, **kwargs)
        cache[key] = res
        return res
    return wrapper


@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(2,3))
print(multiply(2,3))
print(multiply(2,3))
