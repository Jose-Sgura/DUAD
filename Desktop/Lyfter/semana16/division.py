import pytest

def divide(number1, number2):
    
    if not isinstance(number1, (int, float)) or not isinstance(number2, (int, float)):
        raise TypeError("Los parámetros deben ser números, no strings")
    
    
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    
    return number1 / number2

if __name__ == "__main__":
    result = divide(10, 2)
    print(f"10 / 2 = {result}")
