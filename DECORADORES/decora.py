def decorator(f):
    def joining(*arg, **kwargs):
        print("Getting parameter:", arg, kwargs)
        total=f(*arg, **kwargs)
        print("Returning", total)
        return total
    return joining
@decorator
def sm(a,b):
    return a+b
sm(3,4)

def decorator_number(number):
    def wrapper(*args):
        for value in args:
            if not isinstance(value, (int,float)):
                raise TypeError("Only numbers for parameter")
        return number(*args)
    
    return wrapper

@decorator_number
def sum(a,b):
    return a+b

print(sum(3,5))

class User:
    def __init__(self, date_of_birth, age):
        self.date_of_birth=date_of_birth
        self.age=age




