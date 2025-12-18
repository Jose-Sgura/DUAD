from datetime import datetime
print("extra  3")
def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError("Numeric parameters please")
        return func(*args, **kwargs)
    return wrapper

def log_call(call):
    def joined(*args, **kwargs):
        now = datetime.now()
        result = call(*args, **kwargs)
        
        print(f'func:{call.__name__} - args: {args[0]}, {args[1]} - [{now}] - Result: {result}')
        print(f"Result {result}")

        return result
    return joined

@log_call
@validate_numbers
def multiply(a, b):
    return a * b

multiply(3, 4)