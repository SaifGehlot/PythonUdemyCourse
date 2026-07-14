from functools import wraps

def logActivity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@logActivity
def brewChai(type, milk='No!'):
    print(f"Brewing chai {type}, chai and milk status {milk}")

brewChai("Masala")