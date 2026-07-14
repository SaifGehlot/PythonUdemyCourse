from functools import wraps

def myDecorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@myDecorator
def greet():
    print("Hello, From decorator enviroment")

greet()