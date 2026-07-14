from functools import wraps

def requireAdmin(func):
    @wraps(func)
    def wrapper(userRole):
        if userRole != "Admin" :
            print("Access Denied, Admins only")
        else:
            return func(userRole)
        
    return wrapper

@requireAdmin
def accessTeaInventory(role):
    print("Access granted to tea inventory")

accessTeaInventory("user")
accessTeaInventory("Admin")
